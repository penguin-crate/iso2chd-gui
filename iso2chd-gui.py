#!/usr/bin/env python3
import json
import os
import sys
from PyQt6.QtCore import QProcess, Qt, QMimeData
from PyQt6.QtGui import QActionGroup, QColor, QFont, QIcon
from PyQt6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QCheckBox,
    QColorDialog,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QFormLayout,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMenu,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QSpinBox,
    QSplitter,
    QStyle,
    QTableWidget,
    QTableWidgetItem,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

# --- Expanded Preset Themes ---
PRESET_THEMES = {
    "Nord Dark": {
        "BG": "#2e3440",
        "FG": "#d8dee9",
        "ACCENT": "#88c0d0",
        "BTN": "#4c566a",
        "BTN_HOVER": "#5e81ac",
        "INPUT_BG": "#3b4252",
        "LOG_BG": "#1e1e1e",
    },
    "Dracula": {
        "BG": "#282a36",
        "FG": "#f8f8f2",
        "ACCENT": "#bd93f9",
        "BTN": "#44475a",
        "BTN_HOVER": "#6272a4",
        "INPUT_BG": "#383a59",
        "LOG_BG": "#1e1f29",
    },
    "Matrix Green": {
        "BG": "#0d1117",
        "FG": "#00ff66",
        "ACCENT": "#00cc55",
        "BTN": "#161b22",
        "BTN_HOVER": "#21262d",
        "INPUT_BG": "#1f242c",
        "LOG_BG": "#050709",
    },
    "Catppuccin Mocha": {
        "BG": "#1e1e2e",
        "FG": "#cdd6f4",
        "ACCENT": "#f5c2e7",
        "BTN": "#313244",
        "BTN_HOVER": "#45475a",
        "INPUT_BG": "#181825",
        "LOG_BG": "#11111b",
    },
    "Solarized Dark": {
        "BG": "#002b36",
        "FG": "#839496",
        "ACCENT": "#2aa198",
        "BTN": "#073642",
        "BTN_HOVER": "#586e75",
        "INPUT_BG": "#073642",
        "LOG_BG": "#001e26",
    },
    "Cyberpunk Neon": {
        "BG": "#120458",
        "FG": "#ff007f",
        "ACCENT": "#00f0ff",
        "BTN": "#2d006b",
        "BTN_HOVER": "#ff007f",
        "INPUT_BG": "#1b003a",
        "LOG_BG": "#0a0026",
    },
}

FONT_FAMILY = "Noto Sans"
MONO_FONT = "Fira Code, Menlo, Monospace"


class CustomThemeDialog(QDialog):
    """Interactive Color Wheel Picker Dialog for creating dynamic user themes."""

    def __init__(self, current_palette, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Custom Theme Studio")
        self.resize(420, 380)
        self.palette_data = current_palette.copy()
        self.color_buttons = {}

        layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        for key, name in [
            ("BG", "Main Background"),
            ("FG", "Foreground / Text"),
            ("ACCENT", "Accent / Highlight"),
            ("BTN", "Button Color"),
            ("BTN_HOVER", "Button Hover"),
            ("INPUT_BG", "Input Background"),
            ("LOG_BG", "Terminal Log BG"),
        ]:
            btn = QPushButton()
            btn.setFixedWidth(80)
            self.update_btn_color(btn, self.palette_data[key])
            btn.clicked.connect(
                lambda _, k=key, b=btn: self.pick_color(k, b)
            )
            form_layout.addRow(QLabel(f"<b>{name}:</b>"), btn)
            self.color_buttons[key] = btn

        layout.addLayout(form_layout)

        bbox = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok
            | QDialogButtonBox.StandardButton.Cancel
        )
        bbox.accepted.connect(self.accept)
        bbox.rejected.connect(self.reject)
        layout.addWidget(bbox)

    def update_btn_color(self, btn, hex_code):
        btn.setText(hex_code)
        btn.setStyleSheet(
            f"background-color: {hex_code}; color: #000000; border: 1px solid"
            " #888888;"
        )

    def pick_color(self, key, btn):
        color = QColorDialog.getColor(
            QColor(self.palette_data[key]), self, f"Select {key} Color"
        )
        if color.isValid():
            hex_val = color.name()
            self.palette_data[key] = hex_val
            self.update_btn_color(btn, hex_val)

    def get_palette(self):
        return self.palette_data


class Iso2ChdGui(QMainWindow):

    def __init__(self):
        super().__init__()
        self.process = None
        self.active_palette = PRESET_THEMES["Nord Dark"].copy()
        self.current_theme_name = "Nord Dark"
        self.log_font_size = 9
        self.queue_items = []
        self.current_queue_index = -1
        self.size_unit = "Auto"
        
        # New feature metrics tracking
        self.total_input_bytes = 0
        self.total_output_bytes = 0

        self.apply_stylesheet()
        self.initUI()
        self.initMenu()

    def apply_stylesheet(self):
        """Generates dynamic CSS styling from the current active palette."""
        t = self.active_palette
        app_font = QFont(FONT_FAMILY, 10)
        QApplication.setFont(app_font)

        bg_hex = t["BG"].lstrip("#")

        style_sheet = f"""
            QWidget {{
                background-color: {t["BG"]};
                color: {t["FG"]};
            }}
            QLabel {{
                padding: 2px;
            }}
            QLineEdit, QComboBox, QSpinBox {{
                background-color: {t["INPUT_BG"]};
                border: 1px solid {t["BTN"]};
                border-radius: 5px;
                padding: 6px;
                selection-background-color: {t["ACCENT"]};
                color: {t["FG"]};
            }}
            QComboBox::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 25px;
                border-left-width: 1px;
                border-left-color: {t["BTN"]};
                border-left-style: solid;
                border-top-right-radius: 5px;
                border-bottom-right-radius: 5px;
                background-color: {t["BTN"]};
            }}
            QComboBox::down-arrow {{
                image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23{t["FG"].lstrip("#")}'><path d='M7 10l5 5 5-5z'/></svg>");
                width: 14px;
                height: 14px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {t["INPUT_BG"]};
                color: {t["FG"]};
                selection-background-color: {t["ACCENT"]};
                selection-color: {t["BG"]};
                border: 1px solid {t["BTN"]};
            }}
            QCheckBox {{
                spacing: 8px;
            }}
            QCheckBox::indicator {{
                width: 18px;
                height: 18px;
                border-radius: 4px;
                background-color: {t["INPUT_BG"]};
                border: 1px solid {t["BTN"]};
            }}
            QCheckBox::indicator:checked {{
                background-color: {t["ACCENT"]};
                border: 1px solid {t["ACCENT"]};
                image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><path fill='none' stroke='%23{bg_hex}' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round' d='M2 8l4 4 8-8'/></svg>");
            }}
            QPushButton {{
                background-color: {t["BTN"]};
                border: 1px solid {t["BTN"]};
                border-radius: 5px;
                padding: 7px 14px;
                font-weight: bold;
                color: {t["FG"]};
            }}
            QPushButton:hover {{
                background-color: {t["BTN_HOVER"]};
            }}
            QPushButton:pressed {{
                background-color: {t["ACCENT"]};
                color: {t["BG"]};
            }}
            QPushButton:disabled {{
                background-color: {t["INPUT_BG"]};
                color: #777777;
            }}
            QTextEdit, QTableWidget {{
                background-color: {t["LOG_BG"]};
                border: 1px solid {t["BTN"]};
                font-family: {MONO_FONT};
                font-size: {self.log_font_size}pt;
                padding: 5px;
                color: {t["FG"]};
            }}
            QHeaderView::section {{
                background-color: {t["INPUT_BG"]};
                color: {t["FG"]};
                padding: 4px;
                border: 1px solid {t["BTN"]};
                font-weight: bold;
            }}
            QProgressBar {{
                border: 1px solid {t["BTN"]};
                border-radius: 5px;
                text-align: center;
                background-color: {t["INPUT_BG"]};
                color: {t["FG"]};
                font-weight: bold;
            }}
            QProgressBar::chunk {{
                background-color: {t["ACCENT"]};
                border-radius: 4px;
            }}
            QMenuBar {{
                background-color: {t["BG"]};
                color: {t["FG"]};
                border-bottom: 1px solid {t["BTN"]};
            }}
            QMenuBar::item:selected {{
                background-color: {t["BTN_HOVER"]};
            }}
            QMenu {{
                background-color: {t["INPUT_BG"]};
                color: {t["FG"]};
                border: 1px solid {t["BTN"]};
            }}
            QMenu::item:selected {{
                background-color: {t["BTN_HOVER"]};
            }}
            QGroupBox {{
                font-weight: bold;
                color: {t["ACCENT"]};
                border: 1px solid {t["BTN"]};
                border-radius: 6px;
                margin-top: 8px;
                padding-top: 12px;
            }}
            QGroupBox::title {{
                subcontrol-position: top left;
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 4px;
            }}
            QScrollBar:vertical {{
                background: {t["LOG_BG"]};
                width: 10px;
                margin: 0px;
            }}
            QScrollBar::handle:vertical {{
                background: {t["BTN"]};
                border-radius: 5px;
            }}
            QScrollBar::handle:vertical:hover {{
                background: {t["BTN_HOVER"]};
            }}
        """
        QApplication.instance().setStyleSheet(style_sheet)

    def initMenu(self):
        menu_bar = self.menuBar()

        # File Menu
        file_menu = menu_bar.addMenu("&File")
        
        export_log_action = file_menu.addAction("Export Logs...")
        export_log_action.triggered.connect(self.export_logs)
        
        file_menu.addSeparator()
        
        exit_action = file_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)

        # View Menu
        view_menu = menu_bar.addMenu("&View")
        clear_action = view_menu.addAction("Clear Log Output")
        clear_action.triggered.connect(lambda: self.output_log.clear())

        view_menu.addSeparator()

        zoom_in_action = view_menu.addAction("Zoom In Log Font")
        zoom_in_action.triggered.connect(self.zoom_in_log)

        zoom_out_action = view_menu.addAction("Zoom Out Log Font")
        zoom_out_action.triggered.connect(self.zoom_out_log)

        view_menu.addSeparator()

        # File Size Unit Submenu
        size_menu = view_menu.addMenu("File Size Unit")
        self.size_action_group = QActionGroup(self)
        self.size_action_group.setExclusive(True)

        for unit in ["Auto", "Bytes", "KB", "MB", "GB"]:
            action = size_menu.addAction(unit)
            action.setCheckable(True)
            if unit == self.size_unit:
                action.setChecked(True)
            self.size_action_group.addAction(action)
            action.triggered.connect(
                lambda checked, u=unit: self.change_size_unit(u)
            )

        view_menu.addSeparator()

        # Themes Submenu
        themes_menu = view_menu.addMenu("Color Theme")
        self.theme_action_group = QActionGroup(self)
        self.theme_action_group.setExclusive(True)

        for theme_name in PRESET_THEMES.keys():
            action = themes_menu.addAction(theme_name)
            action.setCheckable(True)
            if theme_name == self.current_theme_name:
                action.setChecked(True)
            self.theme_action_group.addAction(action)
            action.triggered.connect(
                lambda checked, tn=theme_name: self.change_preset_theme(tn)
            )

        themes_menu.addSeparator()

        custom_action = themes_menu.addAction("Custom Color Wheel Studio...")
        custom_action.triggered.connect(self.open_custom_theme_studio)

        # About Menu
        about_menu = menu_bar.addMenu("&About")
        about_action = about_menu.addAction("About iso2chd")
        about_action.triggered.connect(self.show_about_dialog)

    def change_preset_theme(self, theme_name):
        self.current_theme_name = theme_name
        self.active_palette = PRESET_THEMES[theme_name].copy()
        self.apply_stylesheet()
        self.output_log.append(f"[System] Switched theme to: {theme_name}")

    def open_custom_theme_studio(self):
        dlg = CustomThemeDialog(self.active_palette, self)
        if dlg.exec() == QDialog.DialogCode.Accepted:
            self.active_palette = dlg.get_palette()
            self.current_theme_name = "Custom Theme"
            self.apply_stylesheet()
            self.output_log.append("[System] Applied Custom Theme.")

    def zoom_in_log(self):
        if self.log_font_size < 16:
            self.log_font_size += 1
            self.apply_stylesheet()

    def zoom_out_log(self):
        if self.log_font_size > 6:
            self.log_font_size -= 1
            self.apply_stylesheet()

    def change_size_unit(self, unit):
        self.size_unit = unit
        self.refresh_queue_table_sizes()
        self.output_log.append(f"[System] File size preference changed to: {unit}")

    def format_size(self, size_bytes):
        if size_bytes is None or size_bytes < 0:
            return "N/A"
        if self.size_unit == "Bytes":
            return f"{size_bytes} B"
        elif self.size_unit == "KB":
            return f"{size_bytes / 1024:.2f} KB"
        elif self.size_unit == "MB":
            return f"{size_bytes / (1024 * 1024):.2f} MB"
        elif self.size_unit == "GB":
            return f"{size_bytes / (1024 * 1024 * 1024):.2f} GB"
        else:  # Auto
            if size_bytes < 1024:
                return f"{size_bytes} B"
            elif size_bytes < 1024 * 1024:
                return f"{size_bytes / 1024:.1f} KB"
            elif size_bytes < 1024 * 1024 * 1024:
                return f"{size_bytes / (1024 * 1024):.1f} MB"
            else:
                return f"{size_bytes / (1024 * 1024 * 1024):.2f} GB"

    def refresh_queue_table_sizes(self):
        for row, item in enumerate(self.queue_items):
            if row < self.queue_table.rowCount():
                formatted = self.format_size(item.get("size_bytes"))
                self.queue_table.setItem(row, 2, QTableWidgetItem(formatted))

    def show_about_dialog(self):
        QMessageBox.about(
            self,
            "About iso2chd GUI",
            (
                "<b>iso2chd GUI v2.0.0</b><br><br>"
                "Enhanced frontend with Multi-file Queueing, Dynamic Theme"
                " Engine, and Thread Control.<br><br>"
                "<b>Author:</b> Abhimanyu Bhadauriya<br>"
                "<b>Email:</b> abhimanyubhadauriyaalt@gmail.com"
            ),
        )

    def initUI(self):
        self.setWindowTitle("iso2chd Advanced Batch Suite")
        self.setWindowIcon(
            self.style().standardIcon(QStyle.StandardPixmap.SP_ComputerIcon)
        )
        self.resize(850, 750)
        
        # Enable Drag and Drop on main window
        self.setAcceptDrops(True)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(15, 15, 15, 15)

        # Splitter to divide Queue/Controls and Log Area
        splitter = QSplitter(Qt.Orientation.Vertical)

        top_widget = QWidget()
        top_layout = QVBoxLayout(top_widget)
        top_layout.setContentsMargins(0, 0, 0, 0)

        # Selection Bar (Directory or File Selector)
        input_group = QGroupBox("Target Selection & Batch Queue (Drag & Drop Supported)")
        input_layout = QVBoxLayout()

        dir_layout = QHBoxLayout()
        self.dir_input = QLineEdit()
        self.dir_input.setPlaceholderText(
            "Select Directory or Add Specific ISO Files to Queue..."
        )

        browse_dir_btn = QPushButton("Browse Dir...")
        browse_dir_btn.setIcon(
            self.style().standardIcon(QStyle.StandardPixmap.SP_DirIcon)
        )
        browse_dir_btn.clicked.connect(self.select_directory)

        add_files_btn = QPushButton("Add Files...")
        add_files_btn.setIcon(
            self.style().standardIcon(QStyle.StandardPixmap.SP_FileIcon)
        )
        add_files_btn.clicked.connect(self.add_files_to_queue)

        dir_layout.addWidget(self.dir_input)
        dir_layout.addWidget(browse_dir_btn)
        dir_layout.addWidget(add_files_btn)
        input_layout.addLayout(dir_layout)

        # Batch File Queue Table
        self.queue_table = QTableWidget(0, 3)
        self.queue_table.setHorizontalHeaderLabels(
            ["Source Target / Path", "Status", "Size"]
        )
        self.queue_table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeMode.Stretch
        )
        self.queue_table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.queue_table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.queue_table.customContextMenuRequested.connect(self.show_queue_context_menu)
        self.queue_table.setMaximumHeight(130)
        input_layout.addWidget(self.queue_table)

        input_group.setLayout(input_layout)
        top_layout.addWidget(input_group)

        # Advanced Settings Group
        options_group = QGroupBox("Conversion Settings & Performance Tuning")
        options_layout = QGridLayout()

        self.keep_files_chk = QCheckBox("Keep source ISO files")
        self.verify_chk = QCheckBox("Verify CHD after creation")
        self.recursive_chk = QCheckBox("Scan subdirectories recursively")
        self.recursive_chk.setChecked(True)

        options_layout.addWidget(self.keep_files_chk, 0, 0)
        options_layout.addWidget(self.verify_chk, 0, 1)
        options_layout.addWidget(self.recursive_chk, 0, 2)

        # Mode Selection & Codec Selection Layout Row
        mode_container = QHBoxLayout()
        mode_label = QLabel("Mode:")
        self.mode_combo = QComboBox()
        self.mode_combo.addItem("Auto (Detect)", "auto")
        self.mode_combo.addItem("DVD Mode (createdvd)", "createdvd")
        self.mode_combo.addItem("CD Mode (createcd)", "createcd")
        mode_container.addWidget(mode_label)
        mode_container.addWidget(self.mode_combo)
        options_layout.addLayout(mode_container, 1, 0)

        # Compression Codec / Strength Selector
        codec_container = QHBoxLayout()
        codec_label = QLabel("Codec:")
        self.codec_combo = QComboBox()
        self.codec_combo.addItem("Default (zlib)", "")
        self.codec_combo.addItem("ZLIB (Standard)", "zlib")
        self.codec_combo.addItem("LZMA (High Comp)", "lzma")
        self.codec_combo.addItem("HUFF (Fast)", "huff")
        codec_container.addWidget(codec_label)
        codec_container.addWidget(self.codec_combo)
        options_layout.addLayout(codec_container, 1, 1)

        # Performance Threads SpinBox & Auto Detect Checkbox
        thread_container = QHBoxLayout()
        thread_label = QLabel("Threads:")
        self.thread_spin = QSpinBox()
        cpu_cores = os.cpu_count() or 4
        self.thread_spin.setRange(1, cpu_cores)
        self.thread_spin.setValue(cpu_cores)
        self.thread_spin.setEnabled(False)
        self.thread_spin.setToolTip(f"Max system cores detected: {cpu_cores}")
        
        self.auto_thread_chk = QCheckBox("Auto Thread")
        self.auto_thread_chk.setChecked(True)
        self.auto_thread_chk.toggled.connect(lambda checked: self.thread_spin.setEnabled(not checked))

        thread_container.addWidget(thread_label)
        thread_container.addWidget(self.thread_spin)
        thread_container.addWidget(self.auto_thread_chk)
        options_layout.addLayout(thread_container, 1, 2)

        # Custom Flag Overrides & Info Checker button
        flags_container = QHBoxLayout()
        flags_label = QLabel("Extra Flags:")
        self.flags_input = QLineEdit()
        self.flags_input.setPlaceholderText("e.g. -hs 2048")
        
        info_check_btn = QPushButton("Run chdman info")
        info_check_btn.setToolTip("Inspect internal headers & hashes of selected CHD")
        info_check_btn.clicked.connect(self.run_chd_info_checker)

        flags_container.addWidget(flags_label)
        flags_container.addWidget(self.flags_input)
        flags_container.addWidget(info_check_btn)
        options_layout.addLayout(flags_container, 2, 0, 1, 3)

        options_group.setLayout(options_layout)
        top_layout.addWidget(options_group)

        # Execution Controls & Live Analytics
        control_layout = QHBoxLayout()
        self.run_btn = QPushButton("Start Batch Processing")
        self.run_btn.setIcon(
            self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay)
        )
        self.run_btn.setMinimumHeight(40)
        self.run_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.run_btn.clicked.connect(self.start_conversion)

        self.stop_btn = QPushButton("Cancel")
        self.stop_btn.setIcon(
            self.style().standardIcon(QStyle.StandardPixmap.SP_MediaStop)
        )
        self.stop_btn.setMinimumHeight(40)
        self.stop_btn.setEnabled(False)
        self.stop_btn.clicked.connect(self.stop_conversion)
        
        # Live Savings Calculator Label
        self.savings_label = QLabel("Storage Saved: 0.0 MB")
        self.savings_label.setStyleSheet("font-weight: bold; color: #88c0d0;")

        control_layout.addWidget(self.run_btn)
        control_layout.addWidget(self.stop_btn)
        control_layout.addWidget(self.savings_label)
        top_layout.addLayout(control_layout)

        # Progress Indicator
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(True)
        top_layout.addWidget(self.progress_bar)

        splitter.addWidget(top_widget)

        # Bottom Section: Log Output
        bottom_widget = QWidget()
        bottom_layout = QVBoxLayout(bottom_widget)
        bottom_layout.setContentsMargins(0, 0, 0, 0)

        log_label = QLabel("Execution Output Log:")
        log_label.setStyleSheet("font-weight: bold;")
        bottom_layout.addWidget(log_label)

        self.output_log = QTextEdit()
        self.output_log.setReadOnly(True)
        self.output_log.append("Ready. Select directory or files to begin.\n")
        bottom_layout.addWidget(self.output_log)

        splitter.addWidget(bottom_widget)
        splitter.setSizes([420, 240])

        main_layout.addWidget(splitter)

    # --- Drag and Drop Handlers ---
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        for url in urls:
            path = url.toLocalFile()
            if os.path.isdir(path):
                self.dir_input.setText(path)
                row = self.queue_table.rowCount()
                self.queue_table.insertRow(row)
                self.queue_table.setItem(row, 0, QTableWidgetItem(path))
                self.queue_table.setItem(row, 1, QTableWidgetItem("Directory"))
                self.queue_table.setItem(row, 2, QTableWidgetItem("N/A"))
                self.queue_items.append({"type": "dir", "path": path, "size_bytes": None})
            elif os.path.isfile(path) and path.lower().endswith(('.iso', '.bin', '.cue', '.chd')):
                file_size = os.path.getsize(path)
                size_str = self.format_size(file_size)
                row = self.queue_table.rowCount()
                self.queue_table.insertRow(row)
                self.queue_table.setItem(row, 0, QTableWidgetItem(path))
                self.queue_table.setItem(row, 1, QTableWidgetItem("Pending"))
                self.queue_table.setItem(row, 2, QTableWidgetItem(size_str))
                self.queue_items.append({"type": "file", "path": path, "size_bytes": file_size})
        event.acceptProposedAction()

    # --- Queue Context Menu & Management ---
    def show_queue_context_menu(self, pos):
        menu = QMenu(self)
        remove_action = menu.addAction("Remove Selected Item")
        clear_queue_action = menu.addAction("Clear Entire Queue")
        
        action = menu.exec(self.queue_table.viewport().mapToGlobal(pos))
        if action == remove_action:
            selected_rows = set(index.row() for index in self.queue_table.selectedIndexes())
            for row in sorted(selected_rows, reverse=True):
                self.queue_table.removeRow(row)
                if row < len(self.queue_items):
                    self.queue_items.pop(row)
        elif action == clear_queue_action:
            self.queue_table.setRowCount(0)
            self.queue_items.clear()
            self.dir_input.clear()

    # --- Additional Feature Methods ---
    def export_logs(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Export Log Output", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(self.output_log.toPlainText())
                self.output_log.append(f"[System] Logs successfully exported to {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error Exporting Log", str(e))

    def run_chd_info_checker(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select CHD File for Verification", "", "CHD Files (*.chd)")
        if file_path:
            self.output_log.append(f"\n[System] Running chdman info on: {file_path}")
            self.process = QProcess(self)
            self.process.setProcessChannelMode(QProcess.ProcessChannelMode.MergedChannels)
            self.process.readyReadStandardOutput.connect(self.handle_stdout)
            self.process.start("chdman", ["info", "-i", file_path])

    def select_directory(self):
        dir_path = QFileDialog.getExistingDirectory(
            self, "Select Directory Containing ISOs", os.path.expanduser("~")
        )
        if dir_path:
            self.dir_input.setText(dir_path)
            self.queue_items.clear()
            self.queue_table.setRowCount(0)

            # Insert Directory target
            row = self.queue_table.rowCount()
            self.queue_table.insertRow(row)
            self.queue_table.setItem(row, 0, QTableWidgetItem(dir_path))
            self.queue_table.setItem(row, 1, QTableWidgetItem("Directory"))
            self.queue_table.setItem(row, 2, QTableWidgetItem("N/A"))
            self.queue_items.append({"type": "dir", "path": dir_path, "size_bytes": None})

    def add_files_to_queue(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Select ISO / BIN Files", "", "Disk Images (*.iso *.bin *.cue *.chd)"
        )
        if files:
            for file_path in files:
                file_size = os.path.getsize(file_path)
                self.total_input_bytes += file_size
                size_str = self.format_size(file_size)
                row = self.queue_table.rowCount()
                self.queue_table.insertRow(row)
                self.queue_table.setItem(row, 0, QTableWidgetItem(file_path))
                self.queue_table.setItem(row, 1, QTableWidgetItem("Pending"))
                self.queue_table.setItem(row, 2, QTableWidgetItem(size_str))
                self.queue_items.append({"type": "file", "path": file_path, "size_bytes": file_size})

    def start_conversion(self):
        if not self.queue_items and not self.dir_input.text().strip():
            self.output_log.append("Error: Selection queue is empty.\n")
            return

        # Fallback if text field has manual entry
        if not self.queue_items and self.dir_input.text().strip():
            path = self.dir_input.text().strip()
            self.queue_items.append({"type": "dir", "path": path, "size_bytes": None})

        # --- Validation: Check if a CHD file was added manually to the queue ---
        for item in self.queue_items:
            if item["type"] == "file" and item["path"].lower().endswith(".chd"):
                error_msg = (
                    f"Conversion Error: Found manually added CHD file '{os.path.basename(item['path'])}'. "
                    "CHD files cannot be converted to CHD. Please remove CHD files from the queue before starting."
                )
                self.output_log.append(f"\n[Error] {error_msg}\n")
                QMessageBox.critical(self, "Invalid Queue Item", error_msg)
                return
        # ----------------------------------------------------------------------

        self.current_queue_index = 0
        self.run_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.progress_bar.setValue(0)
        self.output_log.clear()

        self.process_next_queue_item()

    def process_next_queue_item(self):
        if self.current_queue_index >= len(self.queue_items):
            self.output_log.append(
                "\n=========================================="
            )
            self.output_log.append(
                "    All Tasks Completed Successfully!"
            )
            self.output_log.append(
                "==========================================\n"
            )
            self.progress_bar.setValue(100)
            self.run_btn.setEnabled(True)
            self.stop_btn.setEnabled(False)
            return

        item = self.queue_items[self.current_queue_index]
        target = item["path"]

        # Update Queue Table Status
        if self.queue_table.rowCount() > self.current_queue_index:
            self.queue_table.setItem(
                self.current_queue_index, 1, QTableWidgetItem("Processing...")
            )

        # Update Progress Bar
        pct = int((self.current_queue_index / len(self.queue_items)) * 100)
        self.progress_bar.setValue(pct)

        # Construction of command flags
        cmd_args = [target]

        if self.mode_combo.currentData() != "auto":
            cmd_args.extend(["--mode", self.mode_combo.currentData()])
            
        # Codec configuration flag
        codec_val = self.codec_combo.currentData()
        if codec_val:
            cmd_args.extend(["--codec", codec_val])

        if self.keep_files_chk.isChecked():
            cmd_args.append("--keep")

        if self.verify_chk.isChecked():
            cmd_args.append("--verify")

        if self.recursive_chk.isChecked() and item["type"] == "dir":
            cmd_args.append("--recursive")

        if not self.auto_thread_chk.isChecked() and self.thread_spin.value() > 0:
            cmd_args.extend(["--numprocessors", str(self.thread_spin.value())])

        extra_flags = self.flags_input.text().strip()
        if extra_flags:
            cmd_args.extend(extra_flags.split())

        self.output_log.append(
            f"\n>>> Task [{self.current_queue_index + 1}/{len(self.queue_items)}]: processing {target} <<<"
        )
        self.output_log.append(f"Command: iso2chd {' '.join(cmd_args)}\n")

        self.process = QProcess(self)
        self.process.setProcessChannelMode(
            QProcess.ProcessChannelMode.MergedChannels
        )
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.finished.connect(self.process_finished)

        self.process.start("iso2chd", cmd_args)

    def stop_conversion(self):
        if self.process and self.process.state() == QProcess.ProcessState.Running:
            self.process.kill()
            self.output_log.append("\n[Warning] Process terminated by user.")
            self.run_btn.setEnabled(True)
            self.stop_btn.setEnabled(False)

    def handle_stdout(self):
        data = self.process.readAllStandardOutput()
        output = bytes(data).decode("utf8")
        self.output_log.append(output)
        sb = self.output_log.verticalScrollBar()
        sb.setValue(sb.maximum())

    def process_finished(self, exit_code, exit_status):
        if self.queue_table.rowCount() > self.current_queue_index:
            status_str = (
                "Completed"
                if exit_code == 0
                else f"Failed ({exit_code})"
            )
            self.queue_table.setItem(
                self.current_queue_index, 1, QTableWidgetItem(status_str)
            )
            
            # If a single file converted successfully, estimate space savings dynamically
            item = self.queue_items[self.current_queue_index]
            if exit_code == 0 and item["type"] == "file" and os.path.exists(item["path"]):
                in_size = os.path.getsize(item["path"])
                # Estimate output .chd path and look for file size if available
                chd_path = os.path.splitext(item["path"])[0] + ".chd"
                if os.path.exists(chd_path):
                    out_size = os.path.getsize(chd_path)
                    self.total_output_bytes += out_size
                    saved = max(0, self.total_input_bytes - self.total_output_bytes)
                    self.savings_label.setText(f"Storage Saved: {saved / (1024*1024*1024):.2f} GB")

        self.current_queue_index += 1
        self.process_next_queue_item()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Iso2ChdGui()
    gui.show()
    sys.exit(app.exec())
