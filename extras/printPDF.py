from PySide6.QtGui import QPixmap, QImage, QPainter
from PySide6.QtPrintSupport import QPrinter
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QFileDialog


class PdfPrinter(QGraphicsView):
    def __init__(self, pdf_path):
        super(PdfPrinter, self).__init__()
        # Load PDF using QGraphicsScene
        scene = QGraphicsScene(self)
        scene.setSceneRect(0, 0, 100, 100)
        self.setScene(scene)
        self.load_pdf(pdf_path)
        # Set up printer
        self.printer = QPrinter(QPrinter.HighResolution)
        self.printer.setFullPage(True)
        # Print PDF
        self.print_pdf()
    def load_pdf(self, pdf_path):
        # Load PDF into QGraphicsScene
        image = QImage(pdf_path)
        pixmap = QPixmap.fromImage(image)
        self.scene().clear()
        self.scene().addPixmap(pixmap)
    def print_pdf(self):
        # Render PDF onto printer
        painter = QPainter(self.printer)
        self.scene().render(painter)
        painter.end()

