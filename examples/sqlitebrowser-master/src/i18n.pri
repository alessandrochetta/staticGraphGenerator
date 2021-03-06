# This file is taken from the project https://gitorious.org/qop/qop/.
# For autocompiling qm-files.

#rules to generate ts
isEmpty(QMAKE_LUPDATE) {
	win32: QMAKE_LUPDATE = $$[QT_INSTALL_BINS]/lupdate.exe
	unix {
		QMAKE_LUPDATE = $$[QT_INSTALL_BINS]/lupdate
		!exists($$QMAKE_LUPDATE) { QMAKE_LUPDATE = lupdate-qt4 }
	} else {
		!exists($$QMAKE_LUPDATE) { QMAKE_LUPDATE = lupdate }
	}
}
#limitation: only on ts can be generated
updatets.name = Creating or updating ts-files...
updatets.input = _PRO_FILE_
updatets.output = $$TRANSLATIONS
updatets.commands = $$QMAKE_LUPDATE ${QMAKE_FILE_IN}
updatets.CONFIG += no_link no_clean
QMAKE_EXTRA_COMPILERS += updatets

#rules for ts->qm
isEmpty(QMAKE_LRELEASE) {
#a qm generated by lrelease-qt3 can be used for qt2, qt3, qt4!
	win32: QMAKE_LRELEASE = $$[QT_INSTALL_BINS]/lrelease.exe
	unix {
		QMAKE_LRELEASE = lrelease-qt3
		!exists($$QMAKE_LRELEASE) { QMAKE_LRELEASE = $$[QT_INSTALL_BINS]/lrelease }
		!exists($$QMAKE_LRELEASE) { QMAKE_LRELEASE = lrelease }
		!exists($$QMAKE_LRELEASE) { QMAKE_LRELEASE = lrelease-qt4 }
	} else {
		!exists($$QMAKE_LRELEASE) { QMAKE_LRELEASE = lrelease }
	}
}
updatets.name = Compiling qm-files...
updateqm.input = TRANSLATIONS
updateqm.output = ${QMAKE_FILE_PATH}/${QMAKE_FILE_BASE}.qm
updateqm.commands = $$QMAKE_LRELEASE ${QMAKE_FILE_IN} -qm ${QMAKE_FILE_PATH}/${QMAKE_FILE_BASE}.qm
updateqm.CONFIG += no_link  no_clean target_predeps
QMAKE_EXTRA_COMPILERS += updateqm
