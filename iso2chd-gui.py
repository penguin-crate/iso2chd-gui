#!/usr/bin/env python3
w=enumerate
m='Pending'
n='Directory'
o='auto'
p='Bytes'
q='Auto'
A='#ff007f'
r='#073642'
s='Nord Dark'
d=Exception
U='.chd'
e='N/A'
V='file'
b='dir'
W=len
X=False
R='size_bytes'
N=None
L='type'
M='LOG_BG'
I='path'
K='BTN_HOVER'
J='BG'
G='INPUT_BG'
H='ACCENT'
D=True
E='FG'
B='BTN'
import os as C,sys,re
from PyQt6.QtCore import QProcess as Y,Qt,QMimeData
from PyQt6.QtGui import QActionGroup as t,QColor as x,QFont,QIcon
from PyQt6.QtWidgets import QAbstractItemView as y,QApplication as f,QCheckBox as c,QColorDialog as z,QComboBox as u,QDialog as g,QDialogButtonBox as Z,QFileDialog as a,QFormLayout as A0,QGridLayout as A1,QGroupBox as v,QHBoxLayout as O,QHeaderView as A2,QLabel as P,QLineEdit as h,QListWidget,QListWidgetItem,QMainWindow as A3,QMenu,QMessageBox as i,QProgressBar as A4,QPushButton as Q,QSpinBox as A5,QSplitter as A6,QStyle as S,QTableWidget as A7,QTableWidgetItem as F,QTextEdit as j,QVBoxLayout as T,QWidget as k,QTabWidget as A8
l={s:{J:'#2e3440',E:'#d8dee9',H:'#88c0d0',B:'#4c566a',K:'#5e81ac',G:'#3b4252',M:'#1e1e1e'},'Dracula':{J:'#282a36',E:'#f8f8f2',H:'#bd93f9',B:'#44475a',K:'#6272a4',G:'#383a59',M:'#1e1f29'},'Matrix Green':{J:'#0d1117',E:'#00ff66',H:'#00cc55',B:'#161b22',K:'#21262d',G:'#1f242c',M:'#050709'},'Catppuccin Mocha':{J:'#1e1e2e',E:'#cdd6f4',H:'#f5c2e7',B:'#313244',K:'#45475a',G:'#181825',M:'#11111b'},'Solarized Dark':{J:'#002b36',E:'#839496',H:'#2aa198',B:r,K:'#586e75',G:r,M:'#001e26'},'Cyberpunk Neon':{J:'#120458',E:A,H:'#00f0ff',B:'#2d006b',K:A,G:'#1b003a',M:'#0a0026'}}
A9='Noto Sans'
AA='Fira Code, Menlo, Monospace'
class AB(g):
	def __init__(A,parent=N):super().__init__(parent);A.setWindowTitle('ISO2CHD Changelog & Release History');A.resize(600,500);F=T(A);B=A8(A);C=j();C.setReadOnly(D);C.setPlainText('=== ISO2CHD GUI Release History ===\n\n[v2.0.2] - Latest Enhancements\n• Added robust Multi-file Queueing with drag-and-drop support for ISO, BIN, CUE, and CHD files.\n• Implemented dynamic Theme Engine with presets (Nord Dark, Dracula, Cyberpunk Neon, etc.) and Custom Color Studio.\n• Added Output Destination directory selector integrated smoothly with rsync handling.\n• Added auto and manual thread configuration controls.\n• Real-time percentage progress extraction from chdman output stream mapping to the GUI progress bar.\n• Automatic cleanup of half-made/partial CHD files if conversions fail or are canceled.\n\n[v2.0.0] - Major PyQt6 Modernization\n• Complete architectural rewrite using PyQt6.\n• Introduced modern dark stylesheets and aesthetic layout elements.\n• Added contextual queue menus and log export features.\n\n[v1.0] - Initial Release\n• Basic PyQt5 interface for wrapping chdman commands.\n• Single file conversions and simple directory scanning.');B.addTab(C,'GUI Changelog');E=j();E.setReadOnly(D);E.setPlainText("=== ISO2CHD CUI (CLI) Release History ===\n\n[v1.1.0] - Advanced CLI Engine\n• Added flexible flag injectors (--keep, --verify, --recursive, --mode, --output, --numprocessors).\n• Streamlined stdout carriage-return and newline handler to prevent terminal clutter during batch runs.\n• Enhanced error handling and exit code propagation for robust shell scripting integration.\n\n[v1.0.0] - Initial Command-Line Tool\n• Initial python script to automate MAME's chdman utility for standard ISO-to-CHD conversions.\n• Basic recursive directory parsing and argument parsing.");B.addTab(E,'CUI / CLI Changelog');F.addWidget(B);G=Z(Z.StandardButton.Ok);G.accepted.connect(A.accept);F.addWidget(G)
class AC(g):
	def __init__(A,current_palette,parent=N):
		super().__init__(parent);A.setWindowTitle('Custom Theme Studio');A.resize(420,380);A.palette_data=current_palette.copy();A.color_buttons={};I=T(A);L=A0();N=[(J,'Main Background'),(E,'Foreground / Text'),(H,'Accent / Highlight'),(B,'Button Color'),(K,'Button Hover'),(G,'Input Background'),(M,'Terminal Log BG')]
		for(D,O)in N:C=Q();C.setFixedWidth(80);A.update_btn_color(C,A.palette_data[D]);C.clicked.connect(lambda _,k=D,b=C:A.pick_color(k,b));L.addRow(P(f"<b>{O}:</b>"),C);A.color_buttons[D]=C
		I.addLayout(L);F=Z(Z.StandardButton.Ok|Z.StandardButton.Cancel);F.accepted.connect(A.accept);F.rejected.connect(A.reject);I.addWidget(F)
	def update_btn_color(B,btn,hex_code):A=hex_code;btn.setText(A);btn.setStyleSheet(f"background-color: {A}; color: #000000; border: 1px solid #888888;")
	def pick_color(A,key,btn):
		B=key;C=z.getColor(x(A.palette_data[B]),A,f"Select {B} Color")
		if C.isValid():D=C.name();A.palette_data[B]=D;A.update_btn_color(btn,D)
	def get_palette(A):return A.palette_data
class AD(A3):
	def __init__(A):super().__init__();A.process=N;A.current_theme_name=s;A.active_palette=l[A.current_theme_name].copy();A.log_font_size=9;A.queue_items=[];A.current_queue_index=-1;A.size_unit=q;A.total_input_bytes=0;A.total_output_bytes=0;A.apply_stylesheet();A.init_ui();A.init_menu()
	def apply_stylesheet(C):A=C.active_palette;D=QFont(A9,10);f.setFont(D);I=A[J].lstrip('#');F=f"""
            QWidget {{
                background-color: {A[J]};
                color: {A[E]};
            }}
            QLabel {{
                padding: 2px;
            }}
            QLineEdit, QComboBox, QSpinBox {{
                background-color: {A[G]};
                border: 1px solid {A[B]};
                border-radius: 5px;
                padding: 6px;
                selection-background-color: {A[H]};
                color: {A[E]};
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
                background-color: {A[G]};
                color: {A[E]};
                selection-background-color: {A[H]};
                selection-color: {A[J]};
                border: 1px solid {A[B]};
            }}
            QCheckBox {{
                spacing: 8px;
            }}
            QCheckBox::indicator {{
                width: 18px;
                height: 18px;
                border-radius: 4px;
                background-color: {A[G]};
                border: 1px solid {A[B]};
            }}
            QCheckBox::indicator:checked {{
                background-color: {A[H]};
                border: 1px solid {A[H]};
            }}
            QPushButton {{
                background-color: {A[B]};
                border: 1px solid {A[B]};
                border-radius: 5px;
                padding: 7px 14px;
                font-weight: bold;
                color: {A[E]};
            }}
            QPushButton:hover {{
                background-color: {A[K]};
            }}
            QPushButton:pressed {{
                background-color: {A[H]};
                color: {A[J]};
            }}
            QPushButton:disabled {{
                background-color: {A[G]};
                color: #777777;
            }}
            QTextEdit, QTableWidget {{
                background-color: {A[M]};
                border: 1px solid {A[B]};
                font-family: {AA};
                font-size: {C.log_font_size}pt;
                padding: 5px;
                color: {A[E]};
            }}
            QHeaderView::section {{
                background-color: {A[G]};
                color: {A[E]};
                padding: 4px;
                border: 1px solid {A[B]};
                font-weight: bold;
            }}
            QProgressBar {{
                border: 1px solid {A[B]};
                border-radius: 5px;
                text-align: center;
                background-color: {A[G]};
                color: {A[E]};
                font-weight: bold;
            }}
            QProgressBar::chunk {{
                background-color: {A[H]};
                border-radius: 4px;
            }}
            QMenuBar {{
                background-color: {A[J]};
                color: {A[E]};
                border-bottom: 1px solid {A[B]};
            }}
            QMenuBar::item:selected {{
                background-color: {A[K]};
            }}
            QMenu {{
                background-color: {A[G]};
                color: {A[E]};
                border: 1px solid {A[B]};
            }}
            QMenu::item:selected {{
                background-color: {A[K]};
            }}
            QGroupBox {{
                font-weight: bold;
                color: {A[H]};
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
                background: {A[M]};
                width: 10px;
                margin: 0px;
            }}
            QScrollBar::handle:vertical {{
                background: {A[B]};
                border-radius: 5px;
            }}
            QScrollBar::handle:vertical:hover {{
                background: {A[K]};
            }}
        """;f.instance().setStyleSheet(F)
	def init_menu(A):
		E=A.menuBar();F=E.addMenu('&File');J=F.addAction('Export Logs...');J.triggered.connect(A.export_logs);F.addSeparator();K=F.addAction('Exit');K.triggered.connect(A.close);B=E.addMenu('&View');L=B.addAction('Clear Log Output');L.triggered.connect(lambda:A.output_log.clear());B.addSeparator();M=B.addAction('Zoom In Log Font');M.triggered.connect(A.zoom_in_log);N=B.addAction('Zoom Out Log Font');N.triggered.connect(A.zoom_out_log);B.addSeparator();O=B.addAction('View Changelog...');O.triggered.connect(A.show_changelog_dialog);B.addSeparator();P=B.addMenu('File Size Unit');A.size_action_group=t(A);A.size_action_group.setExclusive(D)
		for G in[q,p,'KB','MB','GB']:
			C=P.addAction(G);C.setCheckable(D)
			if G==A.size_unit:C.setChecked(D)
			A.size_action_group.addAction(C);C.triggered.connect(lambda checked,u=G:A.change_size_unit(u))
		B.addSeparator();H=B.addMenu('Color Theme');A.theme_action_group=t(A);A.theme_action_group.setExclusive(D)
		for I in l.keys():
			C=H.addAction(I);C.setCheckable(D)
			if I==A.current_theme_name:C.setChecked(D)
			A.theme_action_group.addAction(C);C.triggered.connect(lambda checked,tn=I:A.change_preset_theme(tn))
		H.addSeparator();Q=H.addAction('Custom Color Wheel Studio...');Q.triggered.connect(A.open_custom_theme_studio);R=E.addMenu('&About');S=R.addAction('About iso2chd');S.triggered.connect(A.show_about_dialog)
	def show_changelog_dialog(A):B=AB(A);B.exec()
	def change_preset_theme(A,theme_name):B=theme_name;A.current_theme_name=B;A.active_palette=l[B].copy();A.apply_stylesheet();A.output_log.append(f"[System] Switched theme to: {B}")
	def open_custom_theme_studio(A):
		B=AC(A.active_palette,A)
		if B.exec()==g.DialogCode.Accepted:A.active_palette=B.get_palette();A.current_theme_name='Custom Theme';A.apply_stylesheet();A.output_log.append('[System] Applied Custom Theme.')
	def zoom_in_log(A):
		if A.log_font_size<16:A.log_font_size+=1;A.apply_stylesheet()
	def zoom_out_log(A):
		if A.log_font_size>6:A.log_font_size-=1;A.apply_stylesheet()
	def change_size_unit(A,unit):A.size_unit=unit;A.refresh_queue_table_sizes();A.output_log.append(f"[System] File size preference changed to: {unit}")
	def format_size(B,size_bytes):
		A=size_bytes
		if A is N or A<0:return e
		if B.size_unit==p:return f"{A} B"
		elif B.size_unit=='KB':return f"{A/1024:.2f} KB"
		elif B.size_unit=='MB':return f"{A/1048576:.2f} MB"
		elif B.size_unit=='GB':return f"{A/1073741824:.2f} GB"
		if A<1024:return f"{A} B"
		elif A<1048576:return f"{A/1024:.1f} KB"
		elif A<1073741824:return f"{A/1048576:.1f} MB"
		else:return f"{A/1073741824:.2f} GB"
	def refresh_queue_table_sizes(A):
		for(B,C)in w(A.queue_items):
			if B<A.queue_table.rowCount():D=A.format_size(C.get(R));A.queue_table.setItem(B,2,F(D))
	def show_about_dialog(A):i.about(A,'About iso2chd GUI','<b>iso2chd GUI v2.0.2</b><br><br>Enhanced frontend with Multi-file Queueing, Dynamic Theme Engine, Output Destination, and rsync integration.<br><br><b>Author:</b> Abhimanyu Bhadauriya<br><b>Email:</b> abhimanyubhadauriyaalt@gmail.com')
	def init_ui(A):A.setWindowTitle('ISO2CHD Pro');A.setWindowIcon(A.style().standardIcon(S.StandardPixmap.SP_ComputerIcon));A.resize(850,820);A.setAcceptDrops(D);b=k();A.setCentralWidget(b);L=T(b);L.setSpacing(10);L.setContentsMargins(15,15,15,15);F=A6(Qt.Orientation.Vertical);d=k();E=T(d);E.setContentsMargins(0,0,0,0);e=v('Target Selection & Batch Queue (Drag & Drop Supported)');G=T();H=O();A.dir_input=h();A.dir_input.setPlaceholderText('Select Directory or Add Specific ISO Files to Queue...');M=Q('Browse Dir...');M.setIcon(A.style().standardIcon(S.StandardPixmap.SP_DirIcon));M.clicked.connect(A.select_directory);N=Q('Add Files...');N.setIcon(A.style().standardIcon(S.StandardPixmap.SP_FileIcon));N.clicked.connect(A.add_files_to_queue);H.addWidget(A.dir_input);H.addWidget(M);H.addWidget(N);G.addLayout(H);R=O();A.out_dir_input=h();A.out_dir_input.setPlaceholderText('Optional Output Directory (Uses rsync if specified)...');U=Q('Browse Out...');U.setIcon(A.style().standardIcon(S.StandardPixmap.SP_DirIcon));U.clicked.connect(A.select_output_directory);R.addWidget(A.out_dir_input);R.addWidget(U);G.addLayout(R);A.queue_table=A7(0,3);A.queue_table.setHorizontalHeaderLabels(['Source Target / Path','Status','Size']);A.queue_table.horizontalHeader().setSectionResizeMode(0,A2.ResizeMode.Stretch);A.queue_table.setSelectionBehavior(y.SelectionBehavior.SelectRows);A.queue_table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu);A.queue_table.customContextMenuRequested.connect(A.show_queue_context_menu);A.queue_table.setMaximumHeight(130);G.addWidget(A.queue_table);e.setLayout(G);E.addWidget(e);f=v('Conversion Settings & Performance Tuning');B=A1();A.keep_files_chk=c('Keep source ISO files');A.verify_chk=c('Verify CHD after creation');A.recursive_chk=c('Scan subdirectories recursively');A.recursive_chk.setChecked(D);B.addWidget(A.keep_files_chk,0,0);B.addWidget(A.verify_chk,0,1);B.addWidget(A.recursive_chk,0,2);V=O();l=P('Mode:');A.mode_combo=u();A.mode_combo.addItem('Auto (Detect)',o);A.mode_combo.addItem('DVD Mode (createdvd)','createdvd');A.mode_combo.addItem('CD Mode (createcd)','createcd');V.addWidget(l);V.addWidget(A.mode_combo);B.addLayout(V,1,0);W=O();m=P('Codec:');A.codec_combo=u();A.codec_combo.addItem('Default','');A.codec_combo.addItem('ZLIB','zlib');A.codec_combo.addItem('LZMA','lzma');W.addWidget(m);W.addWidget(A.codec_combo);B.addLayout(W,1,1);I=O();n=P('Threads:');A.thread_spin=A5();Y=C.cpu_count()or 4;A.thread_spin.setRange(1,Y);A.thread_spin.setValue(Y);A.thread_spin.setEnabled(X);A.thread_spin.setToolTip(f"Max system cores detected: {Y}");A.auto_thread_chk=c('Auto Thread');A.auto_thread_chk.setChecked(D);A.auto_thread_chk.toggled.connect(lambda checked:A.thread_spin.setEnabled(not checked));I.addWidget(n);I.addWidget(A.thread_spin);I.addWidget(A.auto_thread_chk);B.addLayout(I,1,2);J=O();p=P('Extra Flags:');A.flags_input=h();A.flags_input.setPlaceholderText('e.g. -hs 2048');Z=Q('Run chdman info');Z.setToolTip('Inspect internal headers & hashes of selected CHD');Z.clicked.connect(A.run_chd_info_checker);J.addWidget(p);J.addWidget(A.flags_input);J.addWidget(Z);B.addLayout(J,2,0,1,3);f.setLayout(B);E.addWidget(f);K=O();A.run_btn=Q('Start Batch Processing');A.run_btn.setIcon(A.style().standardIcon(S.StandardPixmap.SP_MediaPlay));A.run_btn.setMinimumHeight(40);A.run_btn.setCursor(Qt.CursorShape.PointingHandCursor);A.run_btn.clicked.connect(A.start_conversion);A.stop_btn=Q('Cancel');A.stop_btn.setIcon(A.style().standardIcon(S.StandardPixmap.SP_MediaStop));A.stop_btn.setMinimumHeight(40);A.stop_btn.setEnabled(X);A.stop_btn.clicked.connect(A.stop_conversion);A.savings_label=P('Storage Saved: 0.0 MB');A.savings_label.setStyleSheet('font-weight: bold; color: #88c0d0;');K.addWidget(A.run_btn);K.addWidget(A.stop_btn);K.addWidget(A.savings_label);E.addLayout(K);A.progress_bar=A4();A.progress_bar.setValue(0);A.progress_bar.setTextVisible(D);E.addWidget(A.progress_bar);F.addWidget(d);g=k();a=T(g);a.setContentsMargins(0,0,0,0);i=P('Execution Output Log:');i.setStyleSheet('font-weight: bold;');a.addWidget(i);A.output_log=j();A.output_log.setReadOnly(D);A.output_log.append('Ready. Select directory or files to begin.\n');a.addWidget(A.output_log);F.addWidget(g);F.setSizes([450,240]);L.addWidget(F)
	def dragEnterEvent(B,event):
		A=event
		if A.mimeData().hasUrls():A.acceptProposedAction()
		else:A.ignore()
	def dropEvent(A,event):
		E=event
		for H in E.mimeData().urls():
			B=H.toLocalFile()
			if C.path.isdir(B):A.dir_input.setText(B);D=A.queue_table.rowCount();A.queue_table.insertRow(D);A.queue_table.setItem(D,0,F(B));A.queue_table.setItem(D,1,F(n));A.queue_table.setItem(D,2,F(e));A.queue_items.append({L:b,I:B,R:N})
			elif C.path.isfile(B)and B.lower().endswith(('.iso','.bin','.cue',U)):G=C.path.getsize(B);J=A.format_size(G);D=A.queue_table.rowCount();A.queue_table.insertRow(D);A.queue_table.setItem(D,0,F(B));A.queue_table.setItem(D,1,F(m));A.queue_table.setItem(D,2,F(J));A.queue_items.append({L:V,I:B,R:G})
		E.acceptProposedAction()
	def show_queue_context_menu(A,pos):
		B=QMenu(A);F=B.addAction('Selected Item');G=B.addAction('Clear Entire Queue');E=B.exec(A.queue_table.viewport().mapToGlobal(pos))
		if E==F:
			H=set(A.row()for A in A.queue_table.selectedIndexes())
			for C in sorted(H,reverse=D):
				A.queue_table.removeRow(C)
				if C<W(A.queue_items):A.queue_items.pop(C)
		elif E==G:A.queue_table.setRowCount(0);A.queue_items.clear();A.dir_input.clear()
	def export_logs(A):
		B,E=a.getSaveFileName(A,'Export Log Output','','Text Files (*.txt);;All Files (*)')
		if B:
			try:
				with open(B,'w',encoding='utf-8')as C:C.write(A.output_log.toPlainText())
				A.output_log.append(f"[System] Logs successfully exported to {B}")
			except d as D:i.critical(A,'Error Exporting Log',str(D))
	def run_chd_info_checker(A):
		B,C=a.getOpenFileName(A,'Select CHD File for Verification','','CHD Files (*.chd)')
		if B:A.output_log.append(f"\n[System] Running chdman info on: {B}");A.process=Y(A);A.process.setProcessChannelMode(Y.ProcessChannelMode.MergedChannels);A.process.readyReadStandardOutput.connect(A.handle_stdout);A.process.start('chdman',['info','-i',B])
	def select_directory(A):
		B=a.getExistingDirectory(A,'Select Directory Containing ISOs',C.path.expanduser('~'))
		if B:A.dir_input.setText(B);A.queue_items.clear();A.queue_table.setRowCount(0);D=A.queue_table.rowCount();A.queue_table.insertRow(D);A.queue_table.setItem(D,0,F(B));A.queue_table.setItem(D,1,F(n));A.queue_table.setItem(D,2,F(e));A.queue_items.append({L:b,I:B,R:N})
	def select_output_directory(A):
		B=a.getExistingDirectory(A,'Select Output Directory for Processed Files',C.path.expanduser('~'))
		if B:A.out_dir_input.setText(B)
	def add_files_to_queue(A):
		G,J=a.getOpenFileNames(A,'Select ISO / BIN Files','','Disk Images (*.iso *.bin *.cue *.chd)')
		if G:
			for D in G:E=C.path.getsize(D);A.total_input_bytes+=E;H=A.format_size(E);B=A.queue_table.rowCount();A.queue_table.insertRow(B);A.queue_table.setItem(B,0,F(D));A.queue_table.setItem(B,1,F(m));A.queue_table.setItem(B,2,F(H));A.queue_items.append({L:V,I:D,R:E})
	def start_conversion(A):
		if not A.queue_items and not A.dir_input.text().strip():A.output_log.append('Error: Selection queue is empty.\n');return
		if not A.queue_items and A.dir_input.text().strip():F=A.dir_input.text().strip();A.queue_items.append({L:b,I:F,R:N})
		for B in A.queue_items:
			if B[L]==V and B[I].lower().endswith(U):E=f"Conversion Error: Found manually added CHD file '{C.path.basename(B[I])}'. CHD files cannot be converted to CHD.";A.output_log.append(f"\n[Error] {E}\n");i.critical(A,'Invalid Queue Item',E);return
		A.current_queue_index=0;A.run_btn.setEnabled(X);A.stop_btn.setEnabled(D);A.progress_bar.setValue(0);A.output_log.clear();A.process_next_queue_item()
	def process_next_queue_item(A):
		if A.current_queue_index>=W(A.queue_items):A.output_log.append('\n==========================================');A.output_log.append('    All Tasks Completed Successfully!');A.output_log.append('==========================================\n');A.progress_bar.setValue(100);A.run_btn.setEnabled(D);A.stop_btn.setEnabled(X);return
		G=A.queue_items[A.current_queue_index];H=G[I]
		if A.queue_table.rowCount()>A.current_queue_index:A.queue_table.setItem(A.current_queue_index,1,F('Processing...'))
		K=int(A.current_queue_index/W(A.queue_items)*100);A.progress_bar.setValue(K);B=[H];E=A.out_dir_input.text().strip()
		if E:B.extend(['--output',E])
		if A.mode_combo.currentData()!=o:B.extend(['--mode',A.mode_combo.currentData()])
		if A.keep_files_chk.isChecked():B.append('--keep')
		if A.verify_chk.isChecked():B.append('--verify')
		if A.recursive_chk.isChecked()and G[L]==b:B.append('--recursive')
		if not A.auto_thread_chk.isChecked()and A.thread_spin.value()>0:B.extend(['--numprocessors',str(A.thread_spin.value())])
		J=A.flags_input.text().strip()
		if J:B.extend(J.split())
		if E:
			if not C.path.exists(E):
				try:C.makedirs(E)
				except d as M:A.output_log.append(f"[Warning] Could not create output directory: {M}")
		A.output_log.append(f"\n>>> Task [{A.current_queue_index+1}/{W(A.queue_items)}]: processing {H} <<<");A.output_log.append(f"Command: iso2chd {" ".join(B)}\n");A.process=Y(A);A.process.setProcessChannelMode(Y.ProcessChannelMode.MergedChannels);A.process.readyReadStandardOutput.connect(A.handle_stdout);A.process.finished.connect(A.process_finished);A.process.start('iso2chd',B)
	def stop_conversion(A):
		if A.process and A.process.state()==Y.ProcessState.Running:A.process.kill();A.output_log.append('\n[Warning] Process terminated by user.');A.cleanup_partial_chd();A.run_btn.setEnabled(D);A.stop_btn.setEnabled(X)
	def cleanup_partial_chd(A):
		if A.current_queue_index<0 or A.current_queue_index>=W(A.queue_items):return
		D=A.queue_items[A.current_queue_index]
		if D[L]==V:
			E=D[I];F=A.out_dir_input.text().strip();G=C.path.splitext(C.path.basename(E))[0]+U;B=C.path.join(F,G)if F else C.path.splitext(E)[0]+U
			if C.path.exists(B):
				try:C.remove(B);A.output_log.append(f"[System] Deleted half-made CHD file: {B}")
				except d as H:A.output_log.append(f"[Warning] Failed to delete half-made CHD file {B}: {H}")
	def handle_stdout(B):
		E='\n';I=B.process.readAllStandardOutput();C=bytes(I).decode('utf8',errors='ignore');F=re.search('([\\d\\.]+)%\\s+complete',C)
		if F:
			try:J=float(F.group(1));B.progress_bar.setValue(int(J))
			except ValueError:pass
		A=B.output_log.textCursor();A.movePosition(A.MoveOperation.End)
		if'\r'in C:
			for D in C.split('\r'):
				if not D:continue
				if E in D:
					K=D.split(E)
					for(L,G)in w(K):
						if L>0:A.insertText(E)
						if G:A.insertText(G)
				else:A.movePosition(A.MoveOperation.StartOfLine,A.MoveMode.KeepAnchor);A.removeSelectedText();A.insertText(D)
		else:A.insertText(C)
		B.output_log.setTextCursor(A);H=B.output_log.verticalScrollBar();H.setValue(H.maximum())
	def process_finished(A,exit_code,exit_status):
		D=exit_code
		if A.queue_table.rowCount()>A.current_queue_index:
			if D==0:E='Completed'
			else:E=f"Failed ({D})";A.cleanup_partial_chd()
			A.queue_table.setItem(A.current_queue_index,1,F(E));B=A.queue_items[A.current_queue_index]
			if D==0 and B[L]==V and C.path.exists(B[I]):
				K=C.path.getsize(B[I]);G=C.path.splitext(B[I])[0]+U
				if C.path.exists(G):H=C.path.getsize(G);A.total_output_bytes+=H;J=max(0,A.total_input_bytes-A.total_output_bytes);A.savings_label.setText(f"Storage Saved: {J/1073741824:.2f} GB")
		A.current_queue_index+=1;A.process_next_queue_item()
if __name__=='__main__':AE=f(sys.argv);AF=AD();AF.show();sys.exit(AE.exec())
