# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['unit.py'],
             binaries=[],
             datas=[('icons','icons'),
                    ('Method1.py','.'),
                    ('method2.py','.'),
                    ('method3.py','.'),
                    ('method4.py','.'),
                    ('Method5.py','.'),
                   ('unittool.ui','.'),
                    ('photo.qrc','.'),
                     ('photo_rc.py','.'),
                                      
                ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
         a.scripts,
         a.binaries,
         a.zipfiles,
         a.datas,
         [],
         name='unit_converter',
         debug=False,
         bootloader_ignore_signals=False,
         strip=False,
         upx=True,
         upx_exclude=[],
         runtime_tmpdir=None,
         console=False,
         icon='unit converter ICON.png' )
