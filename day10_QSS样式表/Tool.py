class QSSTool:
    @staticmethod
    def setQssToObj(file_path, obj):
        with open(file_path, 'r') as f:
            obj.setStyleSheet(f.read())
