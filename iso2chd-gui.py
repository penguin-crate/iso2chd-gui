#!/usr/bin/env python3
u='Pending'
t='Directory'
s='auto'
r='Bytes'
q='Auto'
p='#ff007f'
A='#073642'
o='Nord Dark'
n=Exception
i='.chd'
h='N/A'
a='file'
Z='dir'
Y=len
W=False
S='size_bytes'
R=None
M='type'
L='LOG_BG'
K='path'
J='BTN_HOVER'
I='BG'
H='INPUT_BG'
G='ACCENT'
F=True
C='FG'
B='BTN'
import os as D,sys,re
from PyQt6.QtCore import QProcess as T,Qt,QMimeData
from PyQt6.QtGui import QActionGroup as j,QColor as v,QFont,QIcon
from PyQt6.QtWidgets import QAbstractItemView as w,QApplication as b,QCheckBox as X,QColorDialog as x,QComboBox as k,QDialog as l,QDialogButtonBox as c,QFileDialog as U,QFormLayout as y,QGridLayout as z,QGroupBox as m,QHBoxLayout as N,QHeaderView as A0,QLabel as O,QLineEdit as d,QListWidget,QListWidgetItem,QMainWindow as A1,QMenu,QMessageBox as e,QProgressBar as A2,QPushButton as P,QSpinBox as A3,QSplitter as A4,QStyle as Q,QTableWidget as A5,QTableWidgetItem as E,QTextEdit as A6,QVBoxLayout as V,QWidget as f
g={o:{I:'#2e3440',C:'#d8dee9',G:'#88c0d0',B:'#4c566a',J:'#5e81ac',H:'#3b4252',L:'#1e1e1e'},'Dracula':{I:'#282a36',C:'#f8f8f2',G:'#bd93f9',B:'#44475a',J:'#6272a4',H:'#383a59',L:'#1e1f29'},'Matrix Green':{I:'#0d1117',C:'#00ff66',G:'#00cc55',B:'#161b22',J:'#21262d',H:'#1f242c',L:'#050709'},'Catppuccin Mocha':{I:'#1e1e2e',C:'#cdd6f4',G:'#f5c2e7',B:'#313244',J:'#45475a',H:'#181825',L:'#11111b'},'Solarized Dark':{I:'#002b36',C:'#839496',G:'#2aa198',B:A,J:'#586e75',H:A,L:'#001e26'},'Cyberpunk Neon':{I:'#120458',C:p,G:'#00f0ff',B:'#2d006b',J:p,H:'#1b003a',L:'#0a0026'}}
A7='Noto Sans'
A8='Fira Code, Menlo, Monospace'
class A9(l):
    def __init__(A,current_palette,parent=R):
        super().__init__(parent);A.setWindowTitle('Custom Theme Studio');A.resize(420,380);A.palette_data=current_palette.copy();A.color_buttons={};K=V(A);M=y();N=[(I,'Main Background'),(C,'Foreground / Text'),(G,'Accent / Highlight'),(B,'Button Color'),(J,'Button Hover'),(H,'Input Background'),(L,'Terminal Log BG')]
        for(E,Q)in N:D=P();D.setFixedWidth(80);A.update_btn_color(D,A.palette_data[E]);D.clicked.connect(lambda _,k=E,b=D:A.pick_color(k,b));M.addRow(O(f"<b>{Q}:</b>"),D);A.color_buttons[E]=D
        K.addLayout(M);F=c(c.StandardButton.Ok|c.StandardButton.Cancel);F.accepted.connect(A.accept);F.rejected.connect(A.reject);K.addWidget(F)
    def update_btn_color(B,btn,hex_code):A=hex_code;btn.setText(A);btn.setStyleSheet(f"background-color: {A}; color: #000000; border: 1px solid #888888;")
    def pick_color(A,key,btn):
        B=key;C=x.getColor(v(A.palette_data[B]),A,f"Select {B} Color")
        if C.isValid():D=C.name();A.palette_data[B]=D;A.update_btn_color(btn,D)
    def get_palette(A):return A.palette_data
class AA(A1):
    def __init__(A):super().__init__();A.process=R;A.current_theme_name=o;A.active_palette=g[A.current_theme_name].copy();A.log_font_size=9;A.queue_items=[];A.current_queue_index=-1;A.size_unit=q;A.total_input_bytes=0;A.total_output_bytes=0;A.apply_stylesheet();A.init_ui();A.init_menu()
    def apply_stylesheet(D):A=D.active_palette;E=QFont(A7,10);b.setFont(E);K=A[I].lstrip('#');F=f"""
            QWidget {{
                background-color: {A[I]};
                color: {A[C]};
            }}
            QLabel {{
                padding: 2px;
            }}
            QLineEdit, QComboBox, QSpinBox {{
                background-color: {A[H]};
                border: 1px solid {A[B]};
                border-radius: 5px;
                padding: 6px;
                selection-background-color: {A[G]};
                color: {A[C]};
            }}
            QComboBox::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 25px;
                border-left: 1px solid {A[B]};
                border-top-right-radius: 5px;
                border-bottom-right-radius: 5px;
                background-color: {A[B]};
            }}
            QComboBox QAbstractItemView {{
                background-color: {A[H]};
                color: {A[C]};
                selection-background-color: {A[G]};
                selection-color: {A[I]};
                border: 1px solid {A[B]};
            }}
            QCheckBox {{
                spacing: 8px;
            }}
            QCheckBox::indicator {{
                width: 18px;
                height: 18px;
                border-radius: 4px;
                background-color: {A[H]};
                border: 1px solid {A[B]};
            }}
            QCheckBox::indicator:checked {{
                background-color: {A[G]};
                border: 1px solid {A[G]};
            }}
            QPushButton {{
                background-color: {A[B]};
                border: 1px solid {A[B]};
                border-radius: 5px;
                padding: 7px 14px;
                font-weight: bold;
                color: {A[C]};
            }}
            QPushButton:hover {{
                background-color: {A[J]};
            }}
            QPushButton:pressed {{
                background-color: {A[G]};
                color: {A[I]};
            }}
            QPushButton:disabled {{
                background-color: {A[H]};
                color: #777777;
            }}
            QTextEdit, QTableWidget {{
                background-color: {A[L]};
                border: 1px solid {A[B]};
                font-family: {A8};
                font-size: {D.log_font_size}pt;
                padding: 5px;
                color: {A[C]};
            }}
            QHeaderView::section {{
                background-color: {A[H]};
                color: {A[C]};
                padding: 4px;
                border: 1px solid {A[B]};
                font-weight: bold;
            }}
            QProgressBar {{
                border: 1px solid {A[B]};
                border-radius: 5px;
                text-align: center;
                background-color: {A[H]};
                color: {A[C]};
                font-weight: bold;
            }}
            QProgressBar::chunk {{
                background-color: {A[G]};
                border-radius: 4px;
            }}
            QMenuBar {{
                background-color: {A[I]};
                color: {A[C]};
                border-bottom: 1px solid {A[B]};
            }}
            QMenuBar::item:selected {{
                background-color: {A[J]};
            }}
            QMenu {{
                background-color: {A[H]};
                color: {A[C]};
                border: 1px solid {A[B]};
            }}
            QMenu::item:selected {{
                background-color: {A[J]};
            }}
            QGroupBox {{
                font-weight: bold;
                color: {A[G]};
                border: 1px solid {A[B]};
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
                background: {A[L]};
                width: 10px;
                margin: 0px;
            }}
            QScrollBar::handle:vertical {{
                background: {A[B]};
                border-radius: 5px;
            }}
            QScrollBar::handle:vertical:hover {{
                background: {A[J]};
            }}
        """;b.instance().setStyleSheet(F)
    def init_menu(A):
        D=A.menuBar();E=D.addMenu('&File');J=E.addAction('Export Logs...');J.triggered.connect(A.export_logs);E.addSeparator();K=E.addAction('Exit');K.triggered.connect(A.close);C=D.addMenu('&View');L=C.addAction('Clear Log Output');L.triggered.connect(lambda:A.output_log.clear());C.addSeparator();M=C.addAction('Zoom In Log Font');M.triggered.connect(A.zoom_in_log);N=C.addAction('Zoom Out Log Font');N.triggered.connect(A.zoom_out_log);C.addSeparator();O=C.addMenu('File Size Unit');A.size_action_group=j(A);A.size_action_group.setExclusive(F)
        for G in[q,r,'KB','MB','GB']:
            B=O.addAction(G);B.setCheckable(F)
            if G==A.size_unit:B.setChecked(F)
            A.size_action_group.addAction(B);B.triggered.connect(lambda checked,u=G:A.change_size_unit(u))
        C.addSeparator();H=C.addMenu('Color Theme');A.theme_action_group=j(A);A.theme_action_group.setExclusive(F)
        for I in g.keys():
            B=H.addAction(I);B.setCheckable(F)
            if I==A.current_theme_name:B.setChecked(F)
            A.theme_action_group.addAction(B);B.triggered.connect(lambda checked,tn=I:A.change_preset_theme(tn))
        H.addSeparator();P=H.addAction('Custom Color Wheel Studio...');P.triggered.connect(A.open_custom_theme_studio);Q=D.addMenu('&About');R=Q.addAction('About iso2chd');R.triggered.connect(A.show_about_dialog)
    def change_preset_theme(A,theme_name):B=theme_name;A.current_theme_name=B;A.active_palette=g[B].copy();A.apply_stylesheet();A.output_log.append(f"[System] Switched theme to: {B}")
    def open_custom_theme_studio(A):
        B=A9(A.active_palette,A)
        if B.exec()==l.DialogCode.Accepted:A.active_palette=B.get_palette();A.current_theme_name='Custom Theme';A.apply_stylesheet();A.output_log.append('[System] Applied Custom Theme.')
    def zoom_in_log(A):
        if A.log_font_size<16:A.log_font_size+=1;A.apply_stylesheet()
    def zoom_out_log(A):
        if A.log_font_size>6:A.log_font_size-=1;A.apply_stylesheet()
    def change_size_unit(A,unit):A.size_unit=unit;A.refresh_queue_table_sizes();A.output_log.append(f"[System] File size preference changed to: {unit}")
    def format_size(B,size_bytes):
        A=size_bytes
        if A is R or A<0:return h
        if B.size_unit==r:return f"{A} B"
        elif B.size_unit=='KB':return f"{A/1024:.2f} KB"
        elif B.size_unit=='MB':return f"{A/1048576:.2f} MB"
        elif B.size_unit=='GB':return f"{A/1073741824:.2f} GB"
        if A<1024:return f"{A} B"
        elif A<1048576:return f"{A/1024:.1f} KB"
        elif A<1073741824:return f"{A/1048576:.1f} MB"
        else:return f"{A/1073741824:.2f} GB"
    def refresh_queue_table_sizes(A):
        for(B,C)in enumerate(A.queue_items):
            if B<A.queue_table.rowCount():D=A.format_size(C.get(S));A.queue_table.setItem(B,2,E(D))
    def show_about_dialog(A):e.about(A,'About iso2chd GUI','<b>iso2chd GUI v2.0.2</b><br><br>Enhanced frontend with Multi-file Queueing, Dynamic Theme Engine, Output Destination, and rsync integration.<br><br><b>Author:</b> Abhimanyu Bhadauriya<br><b>Email:</b> abhimanyubhadauriyaalt@gmail.com')
    def init_ui(A):A.setWindowTitle('iso2chd Advanced Batch Suite');A.setWindowIcon(A.style().standardIcon(Q.StandardPixmap.SP_ComputerIcon));A.resize(850,820);A.setAcceptDrops(F);c=f();A.setCentralWidget(c);L=V(c);L.setSpacing(10);L.setContentsMargins(15,15,15,15);E=A4(Qt.Orientation.Vertical);e=f();C=V(e);C.setContentsMargins(0,0,0,0);g=m('Target Selection & Batch Queue (Drag & Drop Supported)');G=V();H=N();A.dir_input=d();A.dir_input.setPlaceholderText('Select Directory or Add Specific ISO Files to Queue...');M=P('Browse Dir...');M.setIcon(A.style().standardIcon(Q.StandardPixmap.SP_DirIcon));M.clicked.connect(A.select_directory);R=P('Add Files...');R.setIcon(A.style().standardIcon(Q.StandardPixmap.SP_FileIcon));R.clicked.connect(A.add_files_to_queue);H.addWidget(A.dir_input);H.addWidget(M);H.addWidget(R);G.addLayout(H);S=N();A.out_dir_input=d();A.out_dir_input.setPlaceholderText('Optional Output Directory (Uses rsync if specified)...');T=P('Browse Out...');T.setIcon(A.style().standardIcon(Q.StandardPixmap.SP_DirIcon));T.clicked.connect(A.select_output_directory);S.addWidget(A.out_dir_input);S.addWidget(T);G.addLayout(S);A.queue_table=A5(0,3);A.queue_table.setHorizontalHeaderLabels(['Source Target / Path','Status','Size']);A.queue_table.horizontalHeader().setSectionResizeMode(0,A0.ResizeMode.Stretch);A.queue_table.setSelectionBehavior(w.SelectionBehavior.SelectRows);A.queue_table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu);A.queue_table.customContextMenuRequested.connect(A.show_queue_context_menu);A.queue_table.setMaximumHeight(130);G.addWidget(A.queue_table);g.setLayout(G);C.addWidget(g);h=m('Conversion Settings & Performance Tuning');B=z();A.keep_files_chk=X('Keep source ISO files');A.verify_chk=X('Verify CHD after creation');A.recursive_chk=X('Scan subdirectories recursively');A.recursive_chk.setChecked(F);B.addWidget(A.keep_files_chk,0,0);B.addWidget(A.verify_chk,0,1);B.addWidget(A.recursive_chk,0,2);U=N();l=O('Mode:');A.mode_combo=k();A.mode_combo.addItem('Auto (Detect)',s);A.mode_combo.addItem('DVD Mode (createdvd)','createdvd');A.mode_combo.addItem('CD Mode (createcd)','createcd');U.addWidget(l);U.addWidget(A.mode_combo);B.addLayout(U,1,0);Y=N();n=O('Codec:');A.codec_combo=k();A.codec_combo.addItem('Default','');A.codec_combo.addItem('ZLIB','zlib');A.codec_combo.addItem('LZMA','lzma');Y.addWidget(n);Y.addWidget(A.codec_combo);B.addLayout(Y,1,1);I=N();o=O('Threads:');A.thread_spin=A3();Z=D.cpu_count()or 4;A.thread_spin.setRange(1,Z);A.thread_spin.setValue(Z);A.thread_spin.setEnabled(W);A.thread_spin.setToolTip(f"Max system cores detected: {Z}");A.auto_thread_chk=X('Auto Thread');A.auto_thread_chk.setChecked(F);A.auto_thread_chk.toggled.connect(lambda checked:A.thread_spin.setEnabled(not checked));I.addWidget(o);I.addWidget(A.thread_spin);I.addWidget(A.auto_thread_chk);B.addLayout(I,1,2);J=N();p=O('Extra Flags:');A.flags_input=d();A.flags_input.setPlaceholderText('e.g. -hs 2048');a=P('Run chdman info');a.setToolTip('Inspect internal headers & hashes of selected CHD');a.clicked.connect(A.run_chd_info_checker);J.addWidget(p);J.addWidget(A.flags_input);J.addWidget(a);B.addLayout(J,2,0,1,3);h.setLayout(B);C.addWidget(h);K=N();A.run_btn=P('Start Batch Processing');A.run_btn.setIcon(A.style().standardIcon(Q.StandardPixmap.SP_MediaPlay));A.run_btn.setMinimumHeight(40);A.run_btn.setCursor(Qt.CursorShape.PointingHandCursor);A.run_btn.clicked.connect(A.start_conversion);A.stop_btn=P('Cancel');A.stop_btn.setIcon(A.style().standardIcon(Q.StandardPixmap.SP_MediaStop));A.stop_btn.setMinimumHeight(40);A.stop_btn.setEnabled(W);A.stop_btn.clicked.connect(A.stop_conversion);A.savings_label=O('Storage Saved: 0.0 MB');A.savings_label.setStyleSheet('font-weight: bold; color: #88c0d0;');K.addWidget(A.run_btn);K.addWidget(A.stop_btn);K.addWidget(A.savings_label);C.addLayout(K);A.progress_bar=A2();A.progress_bar.setValue(0);A.progress_bar.setTextVisible(F);C.addWidget(A.progress_bar);E.addWidget(e);i=f();b=V(i);b.setContentsMargins(0,0,0,0);j=O('Execution Output Log:');j.setStyleSheet('font-weight: bold;');b.addWidget(j);A.output_log=A6();A.output_log.setReadOnly(F);A.output_log.append('Ready. Select directory or files to begin.\n');b.addWidget(A.output_log);E.addWidget(i);E.setSizes([450,240]);L.addWidget(E)
    def dragEnterEvent(B,event):
        A=event
        if A.mimeData().hasUrls():A.acceptProposedAction()
        else:A.ignore()
    def dropEvent(A,event):
        F=event
        for H in F.mimeData().urls():
            B=H.toLocalFile()
            if D.path.isdir(B):A.dir_input.setText(B);C=A.queue_table.rowCount();A.queue_table.insertRow(C);A.queue_table.setItem(C,0,E(B));A.queue_table.setItem(C,1,E(t));A.queue_table.setItem(C,2,E(h));A.queue_items.append({M:Z,K:B,S:R})
            elif D.path.isfile(B)and B.lower().endswith(('.iso','.bin','.cue',i)):G=D.path.getsize(B);I=A.format_size(G);C=A.queue_table.rowCount();A.queue_table.insertRow(C);A.queue_table.setItem(C,0,E(B));A.queue_table.setItem(C,1,E(u));A.queue_table.setItem(C,2,E(I));A.queue_items.append({M:a,K:B,S:G})
        F.acceptProposedAction()
    def show_queue_context_menu(A,pos):
        B=QMenu(A);E=B.addAction('Selected Item');G=B.addAction('Clear Entire Queue');D=B.exec(A.queue_table.viewport().mapToGlobal(pos))
        if D==E:
            H=set(A.row()for A in A.queue_table.selectedIndexes())
            for C in sorted(H,reverse=F):
                A.queue_table.removeRow(C)
                if C<Y(A.queue_items):A.queue_items.pop(C)
        elif D==G:A.queue_table.setRowCount(0);A.queue_items.clear();A.dir_input.clear()
    def export_logs(A):
        B,E=U.getSaveFileName(A,'Export Log Output','','Text Files (*.txt);;All Files (*)')
        if B:
            try:
                with open(B,'w',encoding='utf-8')as C:C.write(A.output_log.toPlainText())
                A.output_log.append(f"[System] Logs successfully exported to {B}")
            except n as D:e.critical(A,'Error Exporting Log',str(D))
    def run_chd_info_checker(A):
        B,C=U.getOpenFileName(A,'Select CHD File for Verification','','CHD Files (*.chd)')
        if B:A.output_log.append(f"\n[System] Running chdman info on: {B}");A.process=T(A);A.process.setProcessChannelMode(T.ProcessChannelMode.MergedChannels);A.process.readyReadStandardOutput.connect(A.handle_stdout);A.process.start('chdman',['info','-i',B])
    def select_directory(A):
        B=U.getExistingDirectory(A,'Select Directory Containing ISOs',D.path.expanduser('~'))
        if B:A.dir_input.setText(B);A.queue_items.clear();A.queue_table.setRowCount(0);C=A.queue_table.rowCount();A.queue_table.insertRow(C);A.queue_table.setItem(C,0,E(B));A.queue_table.setItem(C,1,E(t));A.queue_table.setItem(C,2,E(h));A.queue_items.append({M:Z,K:B,S:R})
    def select_output_directory(A):
        B=U.getExistingDirectory(A,'Select Output Directory for Processed Files',D.path.expanduser('~'))
        if B:A.out_dir_input.setText(B)
    def add_files_to_queue(A):
        G,I=U.getOpenFileNames(A,'Select ISO / BIN Files','','Disk Images (*.iso *.bin *.cue *.chd)')
        if G:
            for C in G:F=D.path.getsize(C);A.total_input_bytes+=F;H=A.format_size(F);B=A.queue_table.rowCount();A.queue_table.insertRow(B);A.queue_table.setItem(B,0,E(C));A.queue_table.setItem(B,1,E(u));A.queue_table.setItem(B,2,E(H));A.queue_items.append({M:a,K:C,S:F})
    def start_conversion(A):
        if not A.queue_items and not A.dir_input.text().strip():A.output_log.append('Error: Selection queue is empty.\n');return
        if not A.queue_items and A.dir_input.text().strip():E=A.dir_input.text().strip();A.queue_items.append({M:Z,K:E,S:R})
        for B in A.queue_items:
            if B[M]==a and B[K].lower().endswith(i):C=f"Conversion Error: Found manually added CHD file '{D.path.basename(B[K])}'. CHD files cannot be converted to CHD.";A.output_log.append(f"\n[Error] {C}\n");e.critical(A,'Invalid Queue Item',C);return
        A.current_queue_index=0;A.run_btn.setEnabled(W);A.stop_btn.setEnabled(F);A.progress_bar.setValue(0);A.output_log.clear();A.process_next_queue_item()
    def process_next_queue_item(A):
        if A.current_queue_index>=Y(A.queue_items):A.output_log.append('\n==========================================');A.output_log.append('    All Tasks Completed Successfully!');A.output_log.append('==========================================\n');A.progress_bar.setValue(100);A.run_btn.setEnabled(F);A.stop_btn.setEnabled(W);return
        G=A.queue_items[A.current_queue_index];H=G[K]
        if A.queue_table.rowCount()>A.current_queue_index:A.queue_table.setItem(A.current_queue_index,1,E('Processing...'))
        J=int(A.current_queue_index/Y(A.queue_items)*100);A.progress_bar.setValue(J);B=[H];C=A.out_dir_input.text().strip()

        # --- FIXED: Append output directory flag if specified ---
        if C:
            B.extend(['--output', C])

        if A.mode_combo.currentData()!=s:B.extend(['--mode',A.mode_combo.currentData()])
        if A.keep_files_chk.isChecked():B.append('--keep')
        if A.verify_chk.isChecked():B.append('--verify')
        if A.recursive_chk.isChecked()and G[M]==Z:B.append('--recursive')
        if not A.auto_thread_chk.isChecked()and A.thread_spin.value()>0:B.extend(['--numprocessors',str(A.thread_spin.value())])
        I=A.flags_input.text().strip()
        if I:B.extend(I.split())
        if C:
            if not D.path.exists(C):
                try:D.makedirs(C)
                except n as L:A.output_log.append(f"[Warning] Could not create output directory: {L}")
        A.output_log.append(f"\n>>> Task [{A.current_queue_index+1}/{Y(A.queue_items)}]: processing {H} <<<");A.output_log.append(f"Command: iso2chd {" ".join(B)}\n");A.process=T(A);A.process.setProcessChannelMode(T.ProcessChannelMode.MergedChannels);A.process.readyReadStandardOutput.connect(A.handle_stdout);A.process.finished.connect(A.process_finished);A.process.start('iso2chd',B)
    def stop_conversion(A):
        if A.process and A.process.state()==T.ProcessState.Running:
            A.process.kill()
            A.output_log.append('\n[Warning] Process terminated by user.')
            A.cleanup_partial_chd()
            A.run_btn.setEnabled(F)
            A.stop_btn.setEnabled(W)
    def cleanup_partial_chd(A):
        if A.current_queue_index<0 or A.current_queue_index>=Y(A.queue_items):return
        B=A.queue_items[A.current_queue_index]
        if B[M]==a:
            C=B[K]
            H=A.out_dir_input.text().strip()
            F=D.path.splitext(D.path.basename(C))[0]+i
            G=D.path.join(H,F) if H else D.path.splitext(C)[0]+i
            if D.path.exists(G):
                try:
                    D.remove(G)
                    A.output_log.append(f"[System] Deleted half-made CHD file: {G}")
                except n as E:
                    A.output_log.append(f"[Warning] Failed to delete half-made CHD file {G}: {E}")
    def handle_stdout(A):
        C=A.process.readAllStandardOutput()
        D_bytes=bytes(C).decode('utf8',errors='ignore')

        # --- FIXED: Parse float progress from output text to update progress bar dynamically ---
        match = re.search(r'([\d\.]+)%\s+complete', D_bytes)
        if match:
            try:
                pct = float(match.group(1))
                A.progress_bar.setValue(int(pct))
            except ValueError:
                pass

        cursor=A.output_log.textCursor()
        cursor.movePosition(cursor.MoveOperation.End)
        if '\r' in D_bytes:
            for chunk in D_bytes.split('\r'):
                if not chunk:continue
                if '\n' in chunk:
                    sub_parts=chunk.split('\n')
                    for idx,sp in enumerate(sub_parts):
                        if idx>0:cursor.insertText('\n')
                        if sp:cursor.insertText(sp)
                else:
                    cursor.movePosition(cursor.MoveOperation.StartOfLine,cursor.MoveMode.KeepAnchor)
                    cursor.removeSelectedText()
                    cursor.insertText(chunk)
        else:
            cursor.insertText(D_bytes)
        A.output_log.setTextCursor(cursor)
        B=A.output_log.verticalScrollBar()
        B.setValue(B.maximum())
    def process_finished(A,exit_code,exit_status):
        C=exit_code
        if A.queue_table.rowCount()>A.current_queue_index:
            if C==0:
                G='Completed'
            else:
                G=f"Failed ({C})"
                A.cleanup_partial_chd()
            A.queue_table.setItem(A.current_queue_index,1,E(G));B=A.queue_items[A.current_queue_index]
            if C==0 and B[M]==a and D.path.exists(B[K]):
                J=D.path.getsize(B[K]);F=D.path.splitext(B[K])[0]+i
                if D.path.exists(F):H=D.path.getsize(F);A.total_output_bytes+=H;I=max(0,A.total_input_bytes-A.total_output_bytes);A.savings_label.setText(f"Storage Saved: {I/1073741824:.2f} GB")
        A.current_queue_index+=1;A.process_next_queue_item()
if __name__=='__main__':AB=b(sys.argv);AC=AA();AC.show();sys.exit(AB.exec())
