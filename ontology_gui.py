import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
    QLineEdit, QComboBox, QHBoxLayout, QFrame, QSpacerItem, QSizePolicy
)
from PySide6.QtGui import QFont, QColor, QPalette
from PySide6.QtCore import Qt
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS

class OntologyApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the Graph
        self.g = Graph()
        self.namespace = URIRef("http://example.org/")
        
        # Initialize the UI
        self.initUI()

    def initUI(self):
        # Set window properties
        self.setWindowTitle('Ontology Manager')
        self.setGeometry(100, 100, 500, 400)

        # Set overall layout
        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Header Section
        header_label = QLabel("Ontology Manager")
        header_label.setFont(QFont("Arial", 20, QFont.Bold))
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet("color: #003366;")
        main_layout.addWidget(header_label)

        # Form Section
        form_frame = QFrame()
        form_frame.setStyleSheet("""
            QFrame {
                border: 2px solid #003366;
                border-radius: 10px;
                background-color: #f4f9ff;
            }
        """)
        form_layout = QVBoxLayout()
        form_layout.setContentsMargins(20, 20, 20, 20)

        # Dropdown for Class Selection
        self.classComboBox = QComboBox(self)
        self.classComboBox.addItems(["Student", "Instructor", "Course"])
        self.classComboBox.setStyleSheet("padding: 5px; font-size: 14px;")
        form_layout.addWidget(QLabel("Select Class:"))
        form_layout.addWidget(self.classComboBox)

        # Input for Name
        self.nameInput = QLineEdit(self)
        self.nameInput.setPlaceholderText("Enter name")
        self.nameInput.setStyleSheet("padding: 5px; font-size: 14px;")
        form_layout.addWidget(QLabel("Enter Name:"))
        form_layout.addWidget(self.nameInput)

        # Input for Age
        self.ageInput = QLineEdit(self)
        self.ageInput.setPlaceholderText("Enter Age")
        self.ageInput.setStyleSheet("padding: 5px; font-size: 14px;")
        form_layout.addWidget(QLabel("Enter Age:"))
        form_layout.addWidget(self.ageInput)

        form_frame.setLayout(form_layout)
        main_layout.addWidget(form_frame)

        # Buttons Section
        button_layout = QHBoxLayout()

        self.createButton = QPushButton('Create Individual', self)
        self.createButton.setStyleSheet("""
            QPushButton {
                background-color: #00509e;
                color: white;
                font-size: 14px;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #003f7d;
            }
        """)
        self.createButton.clicked.connect(self.create_individual)
        button_layout.addWidget(self.createButton)

        self.saveButton = QPushButton('Save Ontology', self)
        self.saveButton.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                font-size: 14px;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        self.saveButton.clicked.connect(self.save_ontology)
        button_layout.addWidget(self.saveButton)

        main_layout.addLayout(button_layout)

        # Spacer
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Output Section
        self.outputLabel = QLabel("", self)
        self.outputLabel.setFont(QFont("Arial", 12))
        self.outputLabel.setStyleSheet("color: #333333;")
        self.outputLabel.setAlignment(Qt.AlignCenter)
        self.outputLabel.setWordWrap(True)
        main_layout.addWidget(self.outputLabel)

        self.setLayout(main_layout)

        # Set window palette
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#e6f2ff"))
        self.setPalette(palette)

    def create_individual(self):
        # Get the class and input values
        selected_class = self.classComboBox.currentText()
        name = self.nameInput.text()
        age = self.ageInput.text()

        if name and age.isdigit():
            # Create the individual in the ontology
            individual = URIRef(self.namespace + name.replace(" ", "_"))
            class_uri = URIRef(self.namespace + selected_class)

            # Add class and properties
            self.g.add((individual, RDF.type, class_uri))
            self.g.add((individual, RDFS.label, Literal(name)))
            self.g.add((individual, URIRef(self.namespace + "age"), Literal(int(age))))

            # Show success message
            self.outputLabel.setText(f"Created {selected_class}: {name}, Age: {age}")

            # Clear input fields
            self.nameInput.clear()
            self.ageInput.clear()

        else:
            self.outputLabel.setText("Please fill in both name and a valid age.")

    def save_ontology(self):
        # Save the updated ontology to a file
        self.g.serialize("updated_ontology.owl", format="xml")
        self.outputLabel.setText("Ontology updated and saved as 'updated_ontology.owl'.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OntologyApp()
    ex.show()
    sys.exit(app.exec())
