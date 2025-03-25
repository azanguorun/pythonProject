import os
# os.system('pyuic5.exe ./UI/register.ui -o register_ui.py -x') #生成可执行文件
# os.system('pyuic5.exe ./UI/login.ui -o login_ui.py -x') #生成可执行文件
os.system('pyuic5.exe ./UI/caculator.ui -o caculator_ui.py -x') #生成可执行文件

# os.system('pyrcc5.exe images.qrc -o images_rc.py') #生成可执行文件
'''
QComboBox{
	font-size:20px;
	border:none;
	border-bottom:1px solid lightgray; 
	background-color:transparent
}
QComboBox:hover{
	border-bottom:1px solid gray; 
}
QComboBox:focus{
	border-bottom:1px solid rgb(92, 255, 160); 
}
QComboBox:drop-down{
	background-color:transparent;
	width:60px;
	height:40px;
}
QComboBox:down_arrow{
	image:url(:/login/images/login_combobox_icon.png);
	width:60px;
	height:20px;
}
QComboBox:QAbstractItemView{
	min-height:60px; 
}
QComboBox:QAbstractItemView:item{
	color:lightblue; 
}


'''