# Cursor Desktop macOS Troubleshooting Guide

This guide covers common issues and solutions for running Cursor desktop on macOS.

## Common Issues and Solutions

### 1. "Cursor.app is damaged and can't be opened" Error

This is the most common issue on macOS. Here are several solutions:

#### Solution A: Copy to Desktop First (Most Effective)
1. Download the Cursor DMG file
2. Open the DMG file
3. **Instead of dragging directly to Applications folder**, copy the Cursor.app file to your Desktop first
4. From Desktop, then move it to Applications folder
5. Launch Cursor from Applications

*This workaround has worked for many users according to community reports.*

#### Solution B: Remove Quarantine Attribute
```bash
xattr -d -r com.apple.quarantine /Applications/Cursor.app
```

#### Solution C: Download Correct Architecture
- For M1/M2/M3 Macs: Download "macOS ARM64" version
- For Intel Macs: Download "macOS x64" version
- Visit the official downloads page to ensure you get the right version

### 2. Installation Using Homebrew (Alternative Method)

If direct installation fails, use Homebrew:

```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Cursor via Homebrew
brew install --cask cursor
```

### 3. "The application 'Install Cursor' can't be opened" Error

#### Solution A: Security Settings
1. Go to `System Preferences` → `Security & Privacy`
2. Ensure "App Store and identified developers" is selected
3. If you see a message about Cursor being blocked, click "Open Anyway"

#### Solution B: Terminal Command
```bash
sudo spctl --master-disable
```
*(Note: This disables Gatekeeper entirely - re-enable after installation)*

### 4. App Freezing/Hanging Issues

If Cursor freezes when opening specific projects:

#### Clear Chat History
Large chat histories can cause freezing. Solutions:

1. **Rename Project Folder** (Quickest fix):
   - Simply rename your project folder to start fresh

2. **Clear Workspace Storage**:
   ```bash
   # Navigate to and delete workspace storage
   rm -rf ~/Library/Application\ Support/Cursor/User/workspaceStorage/*
   ```

3. **Clear All Cursor Data** (Nuclear option):
   ```bash
   # Remove all Cursor data (you'll lose settings and history)
   rm -rf ~/Library/Application\ Support/Cursor/
   rm -rf ~/.cursor
   ```

### 5. Cursor Not Starting After Update

1. **Force quit** any running Cursor processes
2. **Clear cache**:
   ```bash
   rm -rf ~/Library/Application\ Support/Cursor/User/CachedData/
   ```
3. **Restart** Cursor

### 6. macOS Version Compatibility

- **Minimum**: macOS 10.15 (Catalina)
- **Recommended**: Latest macOS version
- If on older macOS, try downloading an older Cursor version

## Download Sources

### Official Sources
- [Cursor Downloads Page](https://www.cursor.com/downloads)
- [GitHub Releases](https://github.com/oslook/cursor-ai-downloads) (Community maintained)

### Homebrew
```bash
brew install --cask cursor
```

## Prevention Tips

1. **Always download from official sources**
2. **Check your Mac architecture** (Intel vs Apple Silicon)
3. **Keep macOS updated**
4. **Regularly clear large chat histories** to prevent freezing
5. **Use the "copy to desktop first" method** for installations

## Still Having Issues?

If none of these solutions work:

1. **Check system logs**:
   - Open Console app
   - Look for Cursor-related errors

2. **Try older version**:
   - Download a previous version that worked

3. **Contact Cursor support**:
   - Visit the [Cursor Community Forum](https://forum.cursor.com/)
   - Report your specific issue with system details

## System Information to Include When Reporting

When reporting issues, include:
- macOS version (e.g., "macOS 14.6.1")
- Mac model (e.g., "MacBook Pro M1 2021")
- Cursor version attempting to install
- Exact error message
- Steps you've already tried

---

*Last updated: January 2025*
*Based on community reports and official documentation*