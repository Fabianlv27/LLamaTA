from tkinter import filedialog


def OpenDirectory():
    filePath=filedialog.askdirectory(
        title="Select a directory"
            )
    return filePath 