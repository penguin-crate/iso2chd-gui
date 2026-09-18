#!/usr/bin/env python3
t='Pending'
s='Directory'
r='auto'
q='Bytes'
p='Auto'
o='#ff007f'
A='#073642'
i='.chd'
h='N/A'
g='Nord Dark'
a='file'
Z='dir'
Y=len
V=False
R='size_bytes'
Q=None
M='type'
L='LOG_BG'
K='path'
J='BTN_HOVER'
I='BG'
G='INPUT_BG'
F='ACCENT'
E=True
C='FG'
B='BTN'
import json,os as H,sys
from PyQt6.QtCore import QProcess as S,Qt,QMimeData
from PyQt6.QtGui import QActionGroup as j,QColor as u,QFont,QIcon
from PyQt6.QtWidgets import QAbstractItemView as v,QApplication as b,QCheckBox as W,QColorDialog as w,QComboBox as k,QDialog as l,QDialogButtonBox as c,QFileDialog as X,QFormLayout as x,QFrame,QGridLayout as y,QGroupBox as m,QHBoxLayout as O,QHeaderView as z,QLabel as N,QLineEdit as n,QListWidget,QListWidgetItem,QMainWindow as A0,QMenu,QMessageBox as d,QProgressBar as A1,QPushButton as P,QSpinBox as A2,QSplitter as A3,QStyle as T,QTableWidget as A4,QTableWidgetItem as D,QTextEdit as A5,QVBoxLayout as U,QWidget as e
f={g:{I:'#2e3440',C:'#d8dee9',F:'#88c0d0',B:'#4c566a',J:'#5e81ac',G:'#3b4252',L:'#1e1e1e'},'Dracula':{I:'#282a36',C:'#f8f8f2',F:'#bd93f9',B:'#44475a',J:'#6272a4',G:'#383a59',L:'#1e1f29'},'Matrix Green':{I:'#0d1117',C:'#00ff66',F:'#00cc55',B:'#161b22',J:'#21262d',G:'#1f242c',L:'#050709'},'Catppuccin Mocha':{I:'#1e1e2e',C:'#cdd6f4',F:'#f5c2e7',B:'#313244',J:'#45475a',G:'#181825',L:'#11111b'},'Solarized Dark':{I:'#002b36',C:'#839496',F:'#2aa198',B:A,J:'#586e75',G:A,L:'#001e26'},'Cyberpunk Neon':{I:'#120458',C:o,F:'#00f0ff',B:'#2d006b',J:o,G:'#1b003a',L:'#0a0026'}}
A6='Noto Sans'
A7='Fira Code, Menlo, Monospace'
class A8(l):
	def __init__(A,current_palette,parent=Q):
		super().__init__(parent);A.setWindowTitle('Custom Theme Studio');A.resize(420,380);A.palette_data=current_palette.copy();A.color_buttons={};K=U(A);M=x()
		for(E,O)in[(I,'Main Background'),(C,'Foreground / Text'),(F,'Accent / Highlight'),(B,'Button Color'),(J,'Button Hover'),(G,'Input Background'),(L,'Terminal Log BG')]:D=P();D.setFixedWidth(80);A.update_btn_color(D,A.palette_data[E]);D.clicked.connect(lambda _,k=E,b=D:A.pick_color(k,b));M.addRow(N(f"<b>{O}:</b>"),D);A.color_buttons[E]=D
		K.addLayout(M);H=c(c.StandardButton.Ok|c.StandardButton.Cancel);H.accepted.connect(A.accept);H.rejected.connect(A.reject);K.addWidget(H)
	def update_btn_color(B,btn,hex_code):A=hex_code;btn.setText(A);btn.setStyleSheet(f"background-color: {A}; color: #000000; border: 1px solid #888888;")
	def pick_color(A,key,btn):
		B=key;C=w.getColor(u(A.palette_data[B]),A,f"Select {B} Color")
		if C.isValid():D=C.name();A.palette_data[B]=D;A.update_btn_color(btn,D)
	def get_palette(A):return A.palette_data
class A9(A0):
	def __init__(A):super().__init__();A.process=Q;A.active_palette=f[g].copy();A.current_theme_name=g;A.log_font_size=9;A.queue_items=[];A.current_queue_index=-1;A.size_unit=p;A.total_input_bytes=0;A.total_output_bytes=0;A.apply_stylesheet();A.initUI();A.initMenu()
	def apply_stylesheet(D):A=D.active_palette;E=QFont(A6,10);b.setFont(E);H=A[I].lstrip('#');K=f"""
            QWidget {{
                background-color: {A[I]};
                color: {A[C]};
            }}
            QLabel {{
                padding: 2px;
            }}
            QLineEdit, QComboBox, QSpinBox {{
                background-color: {A[G]};
                border: 1px solid {A[B]};
                border-radius: 5px;
                padding: 6px;
                selection-background-color: {A[F]};
                color: {A[C]};
            }}
            QComboBox::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 25px;
                border-left-width: 1px;
                border-left-color: {A[B]};
                border-left-style: solid;
                border-top-right-radius: 5px;
                border-bottom-right-radius: 5px;
                background-color: {A[B]};
            }}
            QComboBox::down-arrow {{
                image: url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23{A[C].lstrip("#")}'><path d='M7 10l5 5 5-5z'/></svg>\");
                width: 14px;
                height: 14px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {A[G]};
                color: {A[C]};
                selection-background-color: {A[F]};
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
                background-color: {A[G]};
                border: 1px solid {A[B]};
            }}
            QCheckBox::indicator:checked {{
                background-color: {A[F]};
                border: 1px solid {A[F]};
                image: url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><path fill='none' stroke='%23{H}' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round' d='M2 8l4 4 8-8'/></svg>\");
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
                background-color: {A[F]};
                color: {A[I]};
            }}
            QPushButton:disabled {{
                background-color: {A[G]};
                color: #777777;
            }}
            QTextEdit, QTableWidget {{
                background-color: {A[L]};
                border: 1px solid {A[B]};
                font-family: {A7};
                font-size: {D.log_font_size}pt;
                padding: 5px;
                color: {A[C]};
            }}
            QHeaderView::section {{
                background-color: {A[G]};
                color: {A[C]};
                padding: 4px;
                border: 1px solid {A[B]};
                font-weight: bold;
            }}
            QProgressBar {{
                border: 1px solid {A[B]};
                border-radius: 5px;
                text-align: center;
                background-color: {A[G]};
                color: {A[C]};
                font-weight: bold;
            }}
            QProgressBar::chunk {{
                background-color: {A[F]};
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
                background-color: {A[G]};
                color: {A[C]};
                border: 1px solid {A[B]};
            }}
            QMenu::item:selected {{
                background-color: {A[J]};
            }}
            QGroupBox {{
                font-weight: bold;
                color: {A[F]};
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
        """;b.instance().setStyleSheet(K)
	def initMenu(A):
		D=A.menuBar();F=D.addMenu('&File');J=F.addAction('Export Logs...');J.triggered.connect(A.export_logs);F.addSeparator();K=F.addAction('Exit');K.triggered.connect(A.close);C=D.addMenu('&View');L=C.addAction('Clear Log Output');L.triggered.connect(lambda:A.output_log.clear());C.addSeparator();M=C.addAction('Zoom In Log Font');M.triggered.connect(A.zoom_in_log);N=C.addAction('Zoom Out Log Font');N.triggered.connect(A.zoom_out_log);C.addSeparator();O=C.addMenu('File Size Unit');A.size_action_group=j(A);A.size_action_group.setExclusive(E)
		for G in[p,q,'KB','MB','GB']:
			B=O.addAction(G);B.setCheckable(E)
			if G==A.size_unit:B.setChecked(E)
			A.size_action_group.addAction(B);B.triggered.connect(lambda checked,u=G:A.change_size_unit(u))
		C.addSeparator();H=C.addMenu('Color Theme');A.theme_action_group=j(A);A.theme_action_group.setExclusive(E)
		for I in f.keys():
			B=H.addAction(I);B.setCheckable(E)
			if I==A.current_theme_name:B.setChecked(E)
			A.theme_action_group.addAction(B);B.triggered.connect(lambda checked,tn=I:A.change_preset_theme(tn))
		H.addSeparator();P=H.addAction('Custom Color Wheel Studio...');P.triggered.connect(A.open_custom_theme_studio);Q=D.addMenu('&About');R=Q.addAction('About iso2chd');R.triggered.connect(A.show_about_dialog)
	def change_preset_theme(A,theme_name):B=theme_name;A.current_theme_name=B;A.active_palette=f[B].copy();A.apply_stylesheet();A.output_log.append(f"[System] Switched theme to: {B}")
	def open_custom_theme_studio(A):
		B=A8(A.active_palette,A)
		if B.exec()==l.DialogCode.Accepted:A.active_palette=B.get_palette();A.current_theme_name='Custom Theme';A.apply_stylesheet();A.output_log.append('[System] Applied Custom Theme.')
	def zoom_in_log(A):
		if A.log_font_size<16:A.log_font_size+=1;A.apply_stylesheet()
	def zoom_out_log(A):
		if A.log_font_size>6:A.log_font_size-=1;A.apply_stylesheet()
	def change_size_unit(A,unit):A.size_unit=unit;A.refresh_queue_table_sizes();A.output_log.append(f"[System] File size preference changed to: {unit}")
	def format_size(B,size_bytes):
		A=size_bytes
		if A is Q or A<0:return h
		if B.size_unit==q:return f"{A} B"
		elif B.size_unit=='KB':return f"{A/1024:.2f} KB"
		elif B.size_unit=='MB':return f"{A/1048576:.2f} MB"
		elif B.size_unit=='GB':return f"{A/1073741824:.2f} GB"
		elif A<1024:return f"{A} B"
		elif A<1048576:return f"{A/1024:.1f} KB"
		elif A<1073741824:return f"{A/1048576:.1f} MB"
		else:return f"{A/1073741824:.2f} GB"
	def refresh_queue_table_sizes(A):
		for(B,C)in enumerate(A.queue_items):
			if B<A.queue_table.rowCount():E=A.format_size(C.get(R));A.queue_table.setItem(B,2,D(E))
	def show_about_dialog(A):d.about(A,'About iso2chd GUI','<b>iso2chd GUI v2.0.0</b><br><br>Enhanced frontend with Multi-file Queueing, Dynamic Theme Engine, and Thread Control.<br><br><b>Author:</b> Abhimanyu Bhadauriya<br><b>Email:</b> abhimanyubhadauriyaalt@gmail.com')
	def initUI(A):A.setWindowTitle('iso2chd Advanced Batch Suite');A.setWindowIcon(A.style().standardIcon(T.StandardPixmap.SP_ComputerIcon));A.resize(850,750);A.setAcceptDrops(E);a=e();A.setCentralWidget(a);K=U(a);K.setSpacing(10);K.setContentsMargins(15,15,15,15);D=A3(Qt.Orientation.Vertical);b=e();C=U(b);C.setContentsMargins(0,0,0,0);c=m('Target Selection & Batch Queue (Drag & Drop Supported)');L=U();F=O();A.dir_input=n();A.dir_input.setPlaceholderText('Select Directory or Add Specific ISO Files to Queue...');M=P('Browse Dir...');M.setIcon(A.style().standardIcon(T.StandardPixmap.SP_DirIcon));M.clicked.connect(A.select_directory);Q=P('Add Files...');Q.setIcon(A.style().standardIcon(T.StandardPixmap.SP_FileIcon));Q.clicked.connect(A.add_files_to_queue);F.addWidget(A.dir_input);F.addWidget(M);F.addWidget(Q);L.addLayout(F);A.queue_table=A4(0,3);A.queue_table.setHorizontalHeaderLabels(['Source Target / Path','Status','Size']);A.queue_table.horizontalHeader().setSectionResizeMode(0,z.ResizeMode.Stretch);A.queue_table.setSelectionBehavior(v.SelectionBehavior.SelectRows);A.queue_table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu);A.queue_table.customContextMenuRequested.connect(A.show_queue_context_menu);A.queue_table.setMaximumHeight(130);L.addWidget(A.queue_table);c.setLayout(L);C.addWidget(c);d=m('Conversion Settings & Performance Tuning');B=y();A.keep_files_chk=W('Keep source ISO files');A.verify_chk=W('Verify CHD after creation');A.recursive_chk=W('Scan subdirectories recursively');A.recursive_chk.setChecked(E);B.addWidget(A.keep_files_chk,0,0);B.addWidget(A.verify_chk,0,1);B.addWidget(A.recursive_chk,0,2);R=O();h=N('Mode:');A.mode_combo=k();A.mode_combo.addItem('Auto (Detect)',r);A.mode_combo.addItem('DVD Mode (createdvd)','createdvd');A.mode_combo.addItem('CD Mode (createcd)','createcd');R.addWidget(h);R.addWidget(A.mode_combo);B.addLayout(R,1,0);S=O();i=N('Codec:');A.codec_combo=k();A.codec_combo.addItem('Default (zlib)','');A.codec_combo.addItem('ZLIB (Standard)','zlib');A.codec_combo.addItem('LZMA (High Comp)','lzma');A.codec_combo.addItem('HUFF (Fast)','huff');S.addWidget(i);S.addWidget(A.codec_combo);B.addLayout(S,1,1);G=O();j=N('Threads:');A.thread_spin=A2();X=H.cpu_count()or 4;A.thread_spin.setRange(1,X);A.thread_spin.setValue(X);A.thread_spin.setEnabled(V);A.thread_spin.setToolTip(f"Max system cores detected: {X}");A.auto_thread_chk=W('Auto Thread');A.auto_thread_chk.setChecked(E);A.auto_thread_chk.toggled.connect(lambda checked:A.thread_spin.setEnabled(not checked));G.addWidget(j);G.addWidget(A.thread_spin);G.addWidget(A.auto_thread_chk);B.addLayout(G,1,2);I=O();l=N('Extra Flags:');A.flags_input=n();A.flags_input.setPlaceholderText('e.g. -hs 2048');Y=P('Run chdman info');Y.setToolTip('Inspect internal headers & hashes of selected CHD');Y.clicked.connect(A.run_chd_info_checker);I.addWidget(l);I.addWidget(A.flags_input);I.addWidget(Y);B.addLayout(I,2,0,1,3);d.setLayout(B);C.addWidget(d);J=O();A.run_btn=P('Start Batch Processing');A.run_btn.setIcon(A.style().standardIcon(T.StandardPixmap.SP_MediaPlay));A.run_btn.setMinimumHeight(40);A.run_btn.setCursor(Qt.CursorShape.PointingHandCursor);A.run_btn.clicked.connect(A.start_conversion);A.stop_btn=P('Cancel');A.stop_btn.setIcon(A.style().standardIcon(T.StandardPixmap.SP_MediaStop));A.stop_btn.setMinimumHeight(40);A.stop_btn.setEnabled(V);A.stop_btn.clicked.connect(A.stop_conversion);A.savings_label=N('Storage Saved: 0.0 MB');A.savings_label.setStyleSheet('font-weight: bold; color: #88c0d0;');J.addWidget(A.run_btn);J.addWidget(A.stop_btn);J.addWidget(A.savings_label);C.addLayout(J);A.progress_bar=A1();A.progress_bar.setValue(0);A.progress_bar.setTextVisible(E);C.addWidget(A.progress_bar);D.addWidget(b);f=e();Z=U(f);Z.setContentsMargins(0,0,0,0);g=N('Execution Output Log:');g.setStyleSheet('font-weight: bold;');Z.addWidget(g);A.output_log=A5();A.output_log.setReadOnly(E);A.output_log.append('Ready. Select directory or files to begin.\n');Z.addWidget(A.output_log);D.addWidget(f);D.setSizes([420,240]);K.addWidget(D)
	def dragEnterEvent(B,event):
		A=event
		if A.mimeData().hasUrls():A.acceptProposedAction()
		else:A.ignore()
	def dropEvent(A,event):
		E=event;G=E.mimeData().urls()
		for I in G:
			B=I.toLocalFile()
			if H.path.isdir(B):A.dir_input.setText(B);C=A.queue_table.rowCount();A.queue_table.insertRow(C);A.queue_table.setItem(C,0,D(B));A.queue_table.setItem(C,1,D(s));A.queue_table.setItem(C,2,D(h));A.queue_items.append({M:Z,K:B,R:Q})
			elif H.path.isfile(B)and B.lower().endswith(('.iso','.bin','.cue',i)):F=H.path.getsize(B);J=A.format_size(F);C=A.queue_table.rowCount();A.queue_table.insertRow(C);A.queue_table.setItem(C,0,D(B));A.queue_table.setItem(C,1,D(t));A.queue_table.setItem(C,2,D(J));A.queue_items.append({M:a,K:B,R:F})
		E.acceptProposedAction()
	def show_queue_context_menu(A,pos):
		B=QMenu(A);F=B.addAction('Remove Selected Item');G=B.addAction('Clear Entire Queue');D=B.exec(A.queue_table.viewport().mapToGlobal(pos))
		if D==F:
			H=set(A.row()for A in A.queue_table.selectedIndexes())
			for C in sorted(H,reverse=E):
				A.queue_table.removeRow(C)
				if C<Y(A.queue_items):A.queue_items.pop(C)
		elif D==G:A.queue_table.setRowCount(0);A.queue_items.clear();A.dir_input.clear()
	def export_logs(A):
		B,E=X.getSaveFileName(A,'Export Log Output','','Text Files (*.txt);;All Files (*)')
		if B:
			try:
				with open(B,'w',encoding='utf-8')as C:C.write(A.output_log.toPlainText())
				A.output_log.append(f"[System] Logs successfully exported to {B}")
			except Exception as D:d.critical(A,'Error Exporting Log',str(D))
	def run_chd_info_checker(A):
		B,C=X.getOpenFileName(A,'Select CHD File for Verification','','CHD Files (*.chd)')
		if B:A.output_log.append(f"\n[System] Running chdman info on: {B}");A.process=S(A);A.process.setProcessChannelMode(S.ProcessChannelMode.MergedChannels);A.process.readyReadStandardOutput.connect(A.handle_stdout);A.process.start('chdman',['info','-i',B])
	def select_directory(A):
		B=X.getExistingDirectory(A,'Select Directory Containing ISOs',H.path.expanduser('~'))
		if B:A.dir_input.setText(B);A.queue_items.clear();A.queue_table.setRowCount(0);C=A.queue_table.rowCount();A.queue_table.insertRow(C);A.queue_table.setItem(C,0,D(B));A.queue_table.setItem(C,1,D(s));A.queue_table.setItem(C,2,D(h));A.queue_items.append({M:Z,K:B,R:Q})
	def add_files_to_queue(A):
		F,I=X.getOpenFileNames(A,'Select ISO / BIN Files','','Disk Images (*.iso *.bin *.cue *.chd)')
		if F:
			for C in F:E=H.path.getsize(C);A.total_input_bytes+=E;G=A.format_size(E);B=A.queue_table.rowCount();A.queue_table.insertRow(B);A.queue_table.setItem(B,0,D(C));A.queue_table.setItem(B,1,D(t));A.queue_table.setItem(B,2,D(G));A.queue_items.append({M:a,K:C,R:E})
	def start_conversion(A):
		if not A.queue_items and not A.dir_input.text().strip():A.output_log.append('Error: Selection queue is empty.\n');return
		if not A.queue_items and A.dir_input.text().strip():D=A.dir_input.text().strip();A.queue_items.append({M:Z,K:D,R:Q})
		for B in A.queue_items:
			if B[M]==a and B[K].lower().endswith(i):C=f"Conversion Error: Found manually added CHD file '{H.path.basename(B[K])}'. CHD files cannot be converted to CHD. Please remove CHD files from the queue before starting.";A.output_log.append(f"\n[Error] {C}\n");d.critical(A,'Invalid Queue Item',C);return
		A.current_queue_index=0;A.run_btn.setEnabled(V);A.stop_btn.setEnabled(E);A.progress_bar.setValue(0);A.output_log.clear();A.process_next_queue_item()
	def process_next_queue_item(A):
		if A.current_queue_index>=Y(A.queue_items):A.output_log.append('\n==========================================');A.output_log.append('    All Tasks Completed Successfully!');A.output_log.append('==========================================\n');A.progress_bar.setValue(100);A.run_btn.setEnabled(E);A.stop_btn.setEnabled(V);return
		C=A.queue_items[A.current_queue_index];F=C[K]
		if A.queue_table.rowCount()>A.current_queue_index:A.queue_table.setItem(A.current_queue_index,1,D('Processing...'))
		I=int(A.current_queue_index/Y(A.queue_items)*100);A.progress_bar.setValue(I);B=[F]
		if A.mode_combo.currentData()!=r:B.extend(['--mode',A.mode_combo.currentData()])
		G=A.codec_combo.currentData()
		if G:B.extend(['--codec',G])
		if A.keep_files_chk.isChecked():B.append('--keep')
		if A.verify_chk.isChecked():B.append('--verify')
		if A.recursive_chk.isChecked()and C[M]==Z:B.append('--recursive')
		if not A.auto_thread_chk.isChecked()and A.thread_spin.value()>0:B.extend(['--numprocessors',str(A.thread_spin.value())])
		H=A.flags_input.text().strip()
		if H:B.extend(H.split())
		A.output_log.append(f"\n>>> Task [{A.current_queue_index+1}/{Y(A.queue_items)}]: processing {F} <<<");A.output_log.append(f"Command: iso2chd {" ".join(B)}\n");A.process=S(A);A.process.setProcessChannelMode(S.ProcessChannelMode.MergedChannels);A.process.readyReadStandardOutput.connect(A.handle_stdout);A.process.finished.connect(A.process_finished);A.process.start('iso2chd',B)
	def stop_conversion(A):
		if A.process and A.process.state()==S.ProcessState.Running:A.process.kill();A.output_log.append('\n[Warning] Process terminated by user.');A.run_btn.setEnabled(E);A.stop_btn.setEnabled(V)
	def handle_stdout(A):C=A.process.readAllStandardOutput();D=bytes(C).decode('utf8');A.output_log.append(D);B=A.output_log.verticalScrollBar();B.setValue(B.maximum())
	def process_finished(A,exit_code,exit_status):
		C=exit_code
		if A.queue_table.rowCount()>A.current_queue_index:
			F='Completed'if C==0 else f"Failed ({C})";A.queue_table.setItem(A.current_queue_index,1,D(F));B=A.queue_items[A.current_queue_index]
			if C==0 and B[M]==a and H.path.exists(B[K]):
				J=H.path.getsize(B[K]);E=H.path.splitext(B[K])[0]+i
				if H.path.exists(E):G=H.path.getsize(E);A.total_output_bytes+=G;I=max(0,A.total_input_bytes-A.total_output_bytes);A.savings_label.setText(f"Storage Saved: {I/1073741824:.2f} GB")
		A.current_queue_index+=1;A.process_next_queue_item()
if __name__=='__main__':AA=b(sys.argv);AB=A9();AB.show();sys.exit(AA.exec())
