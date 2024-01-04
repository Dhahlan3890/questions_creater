from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.boxlayout import BoxLayout
from PyPDF2 import PdfReader

class PDFFileSelectorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.file_chooser = FileChooserListView(filters=['*.pdf'])
        select_button = Button(text="Select PDF File", on_press=self.open_file_dialog)

        layout.add_widget(self.file_chooser)
        layout.add_widget(select_button)

        return layout

    def open_file_dialog(self, instance):
        selected_file = self.file_chooser.selection and self.file_chooser.selection[0] or None

        if selected_file:
            print("Selected file:", selected_file)

            # Example: Read the number of pages in the PDF using PyPDF2
            with open(selected_file, 'rb') as file:
                pdf_reader = PdfReader(file)
                num_pages = len(pdf_reader.pages)
                print("Number of pages in the PDF:", num_pages)

if __name__ == '__main__':
    PDFFileSelectorApp().run()
