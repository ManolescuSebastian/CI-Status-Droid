//
//  AppDelegate.swift
//  AndroidStatus
//
//  Created by MSI on 12/01/2020.
//  Copyright © 2020 MSI. All rights reserved.

import Foundation
import Cocoa
import SwiftUI
import ORSSerial

enum ApplicationState {
    case initializationState
    case waitingForPortSelectionState([ORSSerialPort])
    case waitingForBaudRateInputState
    case waitingForUserInputState
}

@NSApplicationMain
class AppDelegate: NSObject, NSApplicationDelegate, ORSSerialPortDelegate {
    
    var window: NSWindow!
    var statusBarItem: NSStatusItem!
    
    var currentSelectedPort : String = ""
    
    func applicationDidFinishLaunching(_ aNotification: Notification) {
        
        let statusBar = NSStatusBar.system
        statusBarItem = statusBar.statusItem(withLength: NSStatusItem.squareLength)
        statusBarItem.button?.title = "🚦"
        
        let statusBarMenu = NSMenu(title: "Show status")
        statusBarItem.menu = statusBarMenu
        
        statusBarMenu.addItem(
            withTitle: "Test Failed",
            action: #selector(AppDelegate.displayAvailableStatus),
            keyEquivalent: "")
        
        statusBarMenu.addItem(
            withTitle: "Test Passed",
            action: #selector(AppDelegate.displayBusyStatus),
            keyEquivalent: "")
        
        let submenu = NSMenu()
        let mainDropdown = NSMenuItem(title: "USB ports", action: nil, keyEquivalent: "")
        statusBarMenu.addItem(mainDropdown)
        statusBarMenu.setSubmenu(submenu, for: mainDropdown)
        
        let availablePorts = ORSSerialPortManager.shared().availablePorts
        
        for port in availablePorts {
            let aSelector = #selector(AppDelegate.portSelector(_:))
            let submenuItem = NSMenuItem(title: port.path, action: aSelector, keyEquivalent: "")
            submenu.addItem(submenuItem)
        }
        
        statusBarMenu.addItem(
            withTitle: "Quit",
            action: #selector(AppDelegate.quitApplication),
            keyEquivalent: "")
    }
    
    @objc func displayBusyStatus() {
        print("Busy sign must be displayed")
        setPortState()
        let value = Data("1".utf8)
        self.handleUserInput(value)
    }
    
    @objc func displayAvailableStatus() {
        print("Available sign must be displayed")
        setPortState()
        let value = Data("2".utf8)
        self.handleUserInput(value)
    }
    
    @objc func portSelector(_ sender: NSMenuItem){
        print(sender.title)
        currentSelectedPort = sender.title
    }
    
    @objc func quitApplication(){
        NSApplication.shared.terminate(self)
    }
    
    
    // MARK: USB communication
    var currentState = ApplicationState.initializationState
    
    var serialPort: ORSSerialPort? {
        didSet {
            serialPort?.delegate = self;
            serialPort?.open()
        }
    }
    
    func setPortState(){
        let availablePorts = ORSSerialPortManager.shared().availablePorts
        currentState = .waitingForPortSelectionState(availablePorts)
    }
    
    // MARK: Port Settings
    func setupAndOpenPortWithSelectionString() -> Bool {
        let serialPort = ORSSerialPort(path: currentSelectedPort)
        print("Current port name: ", currentSelectedPort)
        self.serialPort = serialPort
        return true
    }
    
    // MARK: BaudRate Settings
    func setBaudRateOnPortWithString(_ selectionString: String) -> Bool {
        var selectionString = selectionString
        selectionString = selectionString.trimmingCharacters(in: CharacterSet.whitespacesAndNewlines)
        if let baudRate = Int(selectionString) {
            self.serialPort?.baudRate = NSNumber(value: baudRate)
            print("Baud rate set to \(baudRate)", terminator: "")
            return true
        } else {
            return false
        }
    }
    
    // MARK: Data Processing
    func handleUserInput(_ dataFromUser: Data) {
        
        if !setupAndOpenPortWithSelectionString() {
            print("\nError: Invalid port selection.")
            return
        }
        //case .waitingForBaudRateInputState:
        if !setBaudRateOnPortWithString("9600") {
            print("\nError: Invalid baud rate. Baud rate should consist only of numeric digits.")
            return;
        }
        currentState = .waitingForUserInputState
        self.serialPort?.send(dataFromUser)
    }
    
    // ORSSerialPortDelegate
    func serialPort(_ serialPort: ORSSerialPort, didReceive data: Data) {
        if let string = NSString(data: data, encoding: String.Encoding.utf8.rawValue) {
            print("\nReceived: \"\(string)\" \(data)", terminator: "")
        }
    }
    
    func serialPortWasRemovedFromSystem(_ serialPort: ORSSerialPort) {
        self.serialPort = nil
    }
    
    func serialPort(_ serialPort: ORSSerialPort, didEncounterError error: Error) {
        print("Serial port (\(serialPort)) encountered error: \(error)")
    }
    
    func serialPortWasOpened(_ serialPort: ORSSerialPort) {
        print("Serial port \(serialPort) was opened", terminator: "")
        currentState = .waitingForBaudRateInputState
    }
    
    func applicationWillTerminate(_ aNotification: Notification) {
        // Insert code here to tear down your application
        serialPort?.close()
    }
}
