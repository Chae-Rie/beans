# TestCommit durch jetbrains IDE
import DlgView


def main():
    """In dieser Methode können wir alles an Logik hinzufügen und anschließend wird es in Main getriggered."""
    root = DlgView.tk.Tk()
    app = DlgView.Window_Start(root)
    root.mainloop()


if __name__ == '__main__':
    main()
    