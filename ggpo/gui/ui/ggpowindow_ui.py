# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ggpo/gui/ui/ggpowindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 708)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ggpo/gui/ui/assets/icon-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(3, 0, 3, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.uiSplitter = QtWidgets.QSplitter(self.centralwidget)
        self.uiSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.uiSplitter.setObjectName("uiSplitter")
        self.uiChannelsTree = QtWidgets.QTreeWidget(self.uiSplitter)
        self.uiChannelsTree.setObjectName("uiChannelsTree")
        self.uiChannelsTree.headerItem().setText(0, "#")
        self.uiChannelsTree.headerItem().setTextAlignment(0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.uiChannelsTree.headerItem().setText(1, "Game")
        self.uiChannelsTree.headerItem().setTextAlignment(1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.layoutWidget = QtWidgets.QWidget(self.uiSplitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiChatHistoryTxtB = QtWidgets.QTextBrowser(self.layoutWidget)
        self.uiChatHistoryTxtB.setAcceptDrops(False)
        self.uiChatHistoryTxtB.setReadOnly(True)
        self.uiChatHistoryTxtB.setOpenExternalLinks(False)
        self.uiChatHistoryTxtB.setOpenLinks(False)
        self.uiChatHistoryTxtB.setObjectName("uiChatHistoryTxtB")
        self.verticalLayout.addWidget(self.uiChatHistoryTxtB)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiChatInputEdit = CompletionLineEdit(self.layoutWidget)
        self.uiChatInputEdit.setObjectName("uiChatInputEdit")
        self.horizontalLayout.addWidget(self.uiChatInputEdit)
        self.uiEmoticonTbtn = QtWidgets.QToolButton(self.layoutWidget)
        self.uiEmoticonTbtn.setObjectName("uiEmoticonTbtn")
        self.horizontalLayout.addWidget(self.uiEmoticonTbtn)
        self.uiAfkChk = QtWidgets.QCheckBox(self.layoutWidget)
        self.uiAfkChk.setObjectName("uiAfkChk")
        self.horizontalLayout.addWidget(self.uiAfkChk)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.uiPlayersTableV = QtWidgets.QTableView(self.uiSplitter)
        self.uiPlayersTableV.setObjectName("uiPlayersTableV")
        self.horizontalLayout_2.addWidget(self.uiSplitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 25))
        self.menubar.setObjectName("menubar")
        self.menuAction = QtWidgets.QMenu(self.menubar)
        self.menuAction.setObjectName("menuAction")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.uiThemeMenu = QtWidgets.QMenu(self.menuSetting)
        self.uiThemeMenu.setObjectName("uiThemeMenu")
        self.uiSmoothingMenu = QtWidgets.QMenu(self.menuSetting)
        self.uiSmoothingMenu.setObjectName("uiSmoothingMenu")
        self.menuLogging = QtWidgets.QMenu(self.menuSetting)
        self.menuLogging.setObjectName("menuLogging")
        self.uiChallengeSoundMenu = QtWidgets.QMenu(self.menuSetting)
        self.uiChallengeSoundMenu.setObjectName("uiChallengeSoundMenu")
        self.uiDesktopCompositionMenu = QtWidgets.QMenu(self.menuSetting)
        self.uiDesktopCompositionMenu.setObjectName("uiDesktopCompositionMenu")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.uiStatusbar = QtWidgets.QStatusBar(MainWindow)
        self.uiStatusbar.setObjectName("uiStatusbar")
        MainWindow.setStatusBar(self.uiStatusbar)
        self.uiClearChatHistoryAct = QtWidgets.QAction(MainWindow)
        self.uiClearChatHistoryAct.setObjectName("uiClearChatHistoryAct")
        self.uiAwayAct = QtWidgets.QAction(MainWindow)
        self.uiAwayAct.setCheckable(True)
        self.uiAwayAct.setObjectName("uiAwayAct")
        self.uiQuitAct = QtWidgets.QAction(MainWindow)
        self.uiQuitAct.setObjectName("uiQuitAct")
        self.uiMuteChallengeSoundAct = QtWidgets.QAction(MainWindow)
        self.uiMuteChallengeSoundAct.setCheckable(True)
        self.uiMuteChallengeSoundAct.setObjectName("uiMuteChallengeSoundAct")
        self.uiMuteNotifySoundAct = QtWidgets.QAction(MainWindow)
        self.uiMuteNotifySoundAct.setCheckable(True)
        self.uiMuteNotifySoundAct.setObjectName("uiMuteNotifySoundAct")
        self.uiFontAct = QtWidgets.QAction(MainWindow)
        self.uiFontAct.setObjectName("uiFontAct")
        self.uiAboutAct = QtWidgets.QAction(MainWindow)
        self.uiAboutAct.setObjectName("uiAboutAct")
        self.uiStrevivalAct = QtWidgets.QAction(MainWindow)
        self.uiStrevivalAct.setObjectName("uiStrevivalAct")
        self.uiHitboxViewerAct = QtWidgets.QAction(MainWindow)
        self.uiHitboxViewerAct.setObjectName("uiHitboxViewerAct")
        self.uiSafejumpGuideAct = QtWidgets.QAction(MainWindow)
        self.uiSafejumpGuideAct.setObjectName("uiSafejumpGuideAct")
        self.uiMatchVideosAct = QtWidgets.QAction(MainWindow)
        self.uiMatchVideosAct.setObjectName("uiMatchVideosAct")
        self.uiSRKForumAct = QtWidgets.QAction(MainWindow)
        self.uiSRKForumAct.setObjectName("uiSRKForumAct")
        self.uiSRKWikiAct = QtWidgets.QAction(MainWindow)
        self.uiSRKWikiAct.setObjectName("uiSRKWikiAct")
        self.uiJPWikiAct = QtWidgets.QAction(MainWindow)
        self.uiJPWikiAct.setObjectName("uiJPWikiAct")
        self.uiGNGThemeAct = QtWidgets.QAction(MainWindow)
        self.uiGNGThemeAct.setCheckable(True)
        self.uiGNGThemeAct.setObjectName("uiGNGThemeAct")
        self.uiDarkThemeAct = QtWidgets.QAction(MainWindow)
        self.uiDarkThemeAct.setCheckable(True)
        self.uiDarkThemeAct.setObjectName("uiDarkThemeAct")
        self.uiDebugLogAct = QtWidgets.QAction(MainWindow)
        self.uiDebugLogAct.setCheckable(True)
        self.uiDebugLogAct.setObjectName("uiDebugLogAct")
        self.uiEmoticonAct = QtWidgets.QAction(MainWindow)
        self.uiEmoticonAct.setObjectName("uiEmoticonAct")
        self.uiLocateGgpofbaAct = QtWidgets.QAction(MainWindow)
        self.uiLocateGgpofbaAct.setObjectName("uiLocateGgpofbaAct")
        self.uiLocateROMsAct = QtWidgets.QAction(MainWindow)
        self.uiLocateROMsAct.setObjectName("uiLocateROMsAct")
        self.uiLocateGeommdbAct = QtWidgets.QAction(MainWindow)
        self.uiLocateGeommdbAct.setObjectName("uiLocateGeommdbAct")
        self.uiNotifyPlayerStateChangeAct = QtWidgets.QAction(MainWindow)
        self.uiNotifyPlayerStateChangeAct.setCheckable(True)
        self.uiNotifyPlayerStateChangeAct.setObjectName("uiNotifyPlayerStateChangeAct")
        self.uiFocusOnChatAct = QtWidgets.QAction(MainWindow)
        self.uiFocusOnChatAct.setObjectName("uiFocusOnChatAct")
        self.uiToggleSidebarAction = QtWidgets.QAction(MainWindow)
        self.uiToggleSidebarAction.setObjectName("uiToggleSidebarAction")
        self.uiExpandChannelSidebarAct = QtWidgets.QAction(MainWindow)
        self.uiExpandChannelSidebarAct.setObjectName("uiExpandChannelSidebarAct")
        self.uiContractChannelSidebarAct = QtWidgets.QAction(MainWindow)
        self.uiContractChannelSidebarAct.setObjectName("uiContractChannelSidebarAct")
        self.uiContractPlayerListAct = QtWidgets.QAction(MainWindow)
        self.uiContractPlayerListAct.setObjectName("uiContractPlayerListAct")
        self.uiExpandPlayerListAct = QtWidgets.QAction(MainWindow)
        self.uiExpandPlayerListAct.setObjectName("uiExpandPlayerListAct")
        self.uiLocateUnsupportedSavestatesDirAct = QtWidgets.QAction(MainWindow)
        self.uiLocateUnsupportedSavestatesDirAct.setObjectName("uiLocateUnsupportedSavestatesDirAct")
        self.uiSyncUnsupportedSavestatesAct = QtWidgets.QAction(MainWindow)
        self.uiSyncUnsupportedSavestatesAct.setObjectName("uiSyncUnsupportedSavestatesAct")
        self.uiSelectUnsupportedSavestateAct = QtWidgets.QAction(MainWindow)
        self.uiSelectUnsupportedSavestateAct.setObjectName("uiSelectUnsupportedSavestateAct")
        self.uiFireThemeAct = QtWidgets.QAction(MainWindow)
        self.uiFireThemeAct.setCheckable(True)
        self.uiFireThemeAct.setObjectName("uiFireThemeAct")
        self.uiCustomQssFileAct = QtWidgets.QAction(MainWindow)
        self.uiCustomQssFileAct.setCheckable(True)
        self.uiCustomQssFileAct.setObjectName("uiCustomQssFileAct")
        self.uiNormalThemeAct = QtWidgets.QAction(MainWindow)
        self.uiNormalThemeAct.setCheckable(True)
        self.uiNormalThemeAct.setObjectName("uiNormalThemeAct")
        self.action0 = QtWidgets.QAction(MainWindow)
        self.action0.setObjectName("action0")
        self.uiCustomEmoticonsAct = QtWidgets.QAction(MainWindow)
        self.uiCustomEmoticonsAct.setObjectName("uiCustomEmoticonsAct")
        self.uiShowCountryFlagInChatAct = QtWidgets.QAction(MainWindow)
        self.uiShowCountryFlagInChatAct.setCheckable(True)
        self.uiShowCountryFlagInChatAct.setObjectName("uiShowCountryFlagInChatAct")
        self.uiDisableAutoAnnounceAct = QtWidgets.QAction(MainWindow)
        self.uiDisableAutoAnnounceAct.setCheckable(True)
        self.uiDisableAutoAnnounceAct.setObjectName("uiDisableAutoAnnounceAct")
        self.uiHideGamesWithoutRomAct = QtWidgets.QAction(MainWindow)
        self.uiHideGamesWithoutRomAct.setCheckable(True)
        self.uiHideGamesWithoutRomAct.setObjectName("uiHideGamesWithoutRomAct")
        self.uiShowTimestampInChatAct = QtWidgets.QAction(MainWindow)
        self.uiShowTimestampInChatAct.setCheckable(True)
        self.uiShowTimestampInChatAct.setObjectName("uiShowTimestampInChatAct")
        self.uiDisableAutoColorNicks = QtWidgets.QAction(MainWindow)
        self.uiDisableAutoColorNicks.setCheckable(True)
        self.uiDisableAutoColorNicks.setObjectName("uiDisableAutoColorNicks")
        self.uiLocateCustomChallengeSoundAct = QtWidgets.QAction(MainWindow)
        self.uiLocateCustomChallengeSoundAct.setObjectName("uiLocateCustomChallengeSoundAct")
        self.uiLogChatAct = QtWidgets.QAction(MainWindow)
        self.uiLogChatAct.setCheckable(True)
        self.uiLogChatAct.setObjectName("uiLogChatAct")
        self.uiLogPlayHistoryAct = QtWidgets.QAction(MainWindow)
        self.uiLogPlayHistoryAct.setCheckable(True)
        self.uiLogPlayHistoryAct.setObjectName("uiLogPlayHistoryAct")
        self.uiGNGWebAct = QtWidgets.QAction(MainWindow)
        self.uiGNGWebAct.setObjectName("uiGNGWebAct")
        self.uiFilterFavoriteLobbies = QtWidgets.QAction(MainWindow)
        self.uiFilterFavoriteLobbies.setCheckable(True)
        self.uiFilterFavoriteLobbies.setObjectName("uiFilterFavoriteLobbies")
        self.uiCompositionEnableAct = QtWidgets.QAction(MainWindow)
        self.uiCompositionEnableAct.setObjectName("uiCompositionEnableAct")
        self.uiCompositionDisableAct = QtWidgets.QAction(MainWindow)
        self.uiCompositionDisableAct.setObjectName("uiCompositionDisableAct")
        self.actionReport_an_issue = QtWidgets.QAction(MainWindow)
        self.actionReport_an_issue.setObjectName("actionReport_an_issue")
        self.uiHideInGameChatAct = QtWidgets.QAction(MainWindow)
        self.uiHideInGameChatAct.setCheckable(True)
        self.uiHideInGameChatAct.setObjectName("uiHideInGameChatAct")
        self.menuAction.addAction(self.uiAwayAct)
        self.menuAction.addAction(self.uiFocusOnChatAct)
        self.menuAction.addAction(self.uiEmoticonAct)
        self.menuAction.addAction(self.uiClearChatHistoryAct)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.uiToggleSidebarAction)
        self.menuAction.addAction(self.uiContractChannelSidebarAct)
        self.menuAction.addAction(self.uiExpandChannelSidebarAct)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.uiContractPlayerListAct)
        self.menuAction.addAction(self.uiExpandPlayerListAct)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.uiQuitAct)
        self.menuLogging.addAction(self.uiLogChatAct)
        self.menuLogging.addAction(self.uiLogPlayHistoryAct)
        self.menuLogging.addSeparator()
        self.menuLogging.addAction(self.uiDebugLogAct)
        self.uiChallengeSoundMenu.addAction(self.uiMuteChallengeSoundAct)
        self.uiChallengeSoundMenu.addAction(self.uiLocateCustomChallengeSoundAct)
        self.uiChallengeSoundMenu.addSeparator()
        self.uiDesktopCompositionMenu.addAction(self.uiCompositionEnableAct)
        self.uiDesktopCompositionMenu.addAction(self.uiCompositionDisableAct)
        self.menuSetting.addAction(self.uiMuteNotifySoundAct)
        self.menuSetting.addAction(self.uiChallengeSoundMenu.menuAction())
        self.menuSetting.addAction(self.uiThemeMenu.menuAction())
        self.menuSetting.addAction(self.uiSmoothingMenu.menuAction())
        self.menuSetting.addAction(self.uiDesktopCompositionMenu.menuAction())
        self.menuSetting.addAction(self.uiFontAct)
        self.menuSetting.addAction(self.uiCustomEmoticonsAct)
        self.menuSetting.addSeparator()
        self.menuSetting.addAction(self.uiLocateROMsAct)
        self.menuSetting.addSeparator()
        self.menuSetting.addAction(self.uiNotifyPlayerStateChangeAct)
        self.menuSetting.addAction(self.uiShowCountryFlagInChatAct)
        self.menuSetting.addAction(self.uiShowTimestampInChatAct)
        self.menuSetting.addAction(self.uiHideInGameChatAct)
        self.menuSetting.addAction(self.uiDisableAutoColorNicks)
        self.menuSetting.addAction(self.uiHideGamesWithoutRomAct)
        self.menuSetting.addAction(self.uiFilterFavoriteLobbies)
        self.menuSetting.addAction(self.menuLogging.menuAction())
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.uiGNGWebAct)
        self.menuAbout.addAction(self.actionReport_an_issue)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.uiAboutAct)
        self.menubar.addAction(self.menuAction.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.uiQuitAct.triggered.connect(MainWindow.close)
        self.uiClearChatHistoryAct.triggered.connect(self.uiChatHistoryTxtB.clear)
        self.uiAwayAct.toggled['bool'].connect(self.uiAfkChk.setChecked)
        self.uiAfkChk.clicked.connect(self.uiAwayAct.trigger)
        self.uiFocusOnChatAct.triggered.connect(self.uiChatInputEdit.setFocus)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FightCade"))
        self.uiEmoticonTbtn.setText(_translate("MainWindow", ":)"))
        self.uiAfkChk.setText(_translate("MainWindow", "away"))
        self.menuAction.setTitle(_translate("MainWindow", "&Action"))
        self.menuSetting.setTitle(_translate("MainWindow", "S&ettings"))
        self.uiThemeMenu.setTitle(_translate("MainWindow", "&Theme"))
        self.uiSmoothingMenu.setTitle(_translate("MainWindow", "Smoothing / Input &lag"))
        self.menuLogging.setTitle(_translate("MainWindow", "Logging"))
        self.uiChallengeSoundMenu.setTitle(_translate("MainWindow", "Challenge Sound"))
        self.uiDesktopCompositionMenu.setTitle(_translate("MainWindow", "Desktop Composition"))
        self.menuAbout.setTitle(_translate("MainWindow", "&Help"))
        self.uiClearChatHistoryAct.setText(_translate("MainWindow", "Clear chat his&tory"))
        self.uiClearChatHistoryAct.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.uiAwayAct.setText(_translate("MainWindow", "Away from k&eyboard"))
        self.uiAwayAct.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.uiQuitAct.setText(_translate("MainWindow", "&Quit"))
        self.uiQuitAct.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.uiMuteChallengeSoundAct.setText(_translate("MainWindow", "&Mute Challenge Sound"))
        self.uiMuteChallengeSoundAct.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.uiMuteNotifySoundAct.setText(_translate("MainWindow", "Mute Notify Sound"))
        self.uiFontAct.setText(_translate("MainWindow", "&Font"))
        self.uiAboutAct.setText(_translate("MainWindow", "&About"))
        self.uiStrevivalAct.setText(_translate("MainWindow", "Strategy && &News"))
        self.uiHitboxViewerAct.setText(_translate("MainWindow", "Hitbox &Viewer"))
        self.uiSafejumpGuideAct.setText(_translate("MainWindow", "&Safejump Guide"))
        self.uiMatchVideosAct.setText(_translate("MainWindow", "&Match Videos"))
        self.uiSRKForumAct.setText(_translate("MainWindow", "Shoryuken &Forum"))
        self.uiSRKWikiAct.setText(_translate("MainWindow", "Wiki (English)"))
        self.uiJPWikiAct.setText(_translate("MainWindow", "Wiki (Japanese)"))
        self.uiGNGThemeAct.setText(_translate("MainWindow", "&FightCade"))
        self.uiDarkThemeAct.setText(_translate("MainWindow", "&Dark Orange"))
        self.uiDebugLogAct.setText(_translate("MainWindow", "Debug &Log"))
        self.uiEmoticonAct.setText(_translate("MainWindow", "&Insert Emoticon"))
        self.uiEmoticonAct.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.uiLocateGgpofbaAct.setText(_translate("MainWindow", "&Locate ggpofba-ng.exe"))
        self.uiLocateROMsAct.setText(_translate("MainWindow", "Locate &ROMs Folder"))
        self.uiLocateGeommdbAct.setText(_translate("MainWindow", "Locate &GeoIP mmdb"))
        self.uiNotifyPlayerStateChangeAct.setText(_translate("MainWindow", "&Notify Player State Change"))
        self.uiFocusOnChatAct.setText(_translate("MainWindow", "Foc&us on chat"))
        self.uiFocusOnChatAct.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.uiToggleSidebarAction.setText(_translate("MainWindow", "To&ggle Channel Sidebar"))
        self.uiToggleSidebarAction.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.uiExpandChannelSidebarAct.setText(_translate("MainWindow", "&+ Expand Channel Sidebar"))
        self.uiExpandChannelSidebarAct.setShortcut(_translate("MainWindow", "Ctrl+="))
        self.uiContractChannelSidebarAct.setText(_translate("MainWindow", "&- Contract Channel Sidebar"))
        self.uiContractChannelSidebarAct.setShortcut(_translate("MainWindow", "Ctrl+-"))
        self.uiContractPlayerListAct.setText(_translate("MainWindow", "&> Contract Player List"))
        self.uiContractPlayerListAct.setShortcut(_translate("MainWindow", "Ctrl+."))
        self.uiExpandPlayerListAct.setText(_translate("MainWindow", "&< Expand Player List"))
        self.uiExpandPlayerListAct.setShortcut(_translate("MainWindow", "Ctrl+,"))
        self.uiLocateUnsupportedSavestatesDirAct.setText(_translate("MainWindow", "Locate &Unsupported Savestates Directory"))
        self.uiSyncUnsupportedSavestatesAct.setText(_translate("MainWindow", "S&ync Unsupported Savestates"))
        self.uiSelectUnsupportedSavestateAct.setText(_translate("MainWindow", "&Select Unsupported Savestate"))
        self.uiSelectUnsupportedSavestateAct.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.uiFireThemeAct.setText(_translate("MainWindow", "&Fire"))
        self.uiCustomQssFileAct.setText(_translate("MainWindow", "Custom Qss File"))
        self.uiNormalThemeAct.setText(_translate("MainWindow", "&Normal"))
        self.action0.setText(_translate("MainWindow", "0"))
        self.uiCustomEmoticonsAct.setText(_translate("MainWindow", "Custom &Emoticons"))
        self.uiShowCountryFlagInChatAct.setText(_translate("MainWindow", "Show Country Flag in Chat"))
        self.uiDisableAutoAnnounceAct.setText(_translate("MainWindow", "&Disable auto announce in unsupported room"))
        self.uiHideGamesWithoutRomAct.setText(_translate("MainWindow", "Hide Games with Missing ROMs"))
        self.uiShowTimestampInChatAct.setText(_translate("MainWindow", "Show Timestamp in Chat"))
        self.uiDisableAutoColorNicks.setText(_translate("MainWindow", "Disable auto-color of Nicknames"))
        self.uiLocateCustomChallengeSoundAct.setText(_translate("MainWindow", "Custom Challenge Sound"))
        self.uiLogChatAct.setText(_translate("MainWindow", "Chat history"))
        self.uiLogPlayHistoryAct.setText(_translate("MainWindow", "Play history"))
        self.uiGNGWebAct.setText(_translate("MainWindow", "FightCade website"))
        self.uiFilterFavoriteLobbies.setText(_translate("MainWindow", "Filter Favorite Lobbies"))
        self.uiCompositionEnableAct.setText(_translate("MainWindow", "Enable"))
        self.uiCompositionDisableAct.setText(_translate("MainWindow", "Disable (Recommended)"))
        self.actionReport_an_issue.setText(_translate("MainWindow", "Report an issue"))
        self.uiHideInGameChatAct.setText(_translate("MainWindow", "Hide in-game Chat on Lobby"))
from ggpo.gui.completionlineedit import CompletionLineEdit
