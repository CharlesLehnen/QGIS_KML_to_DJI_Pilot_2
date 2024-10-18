import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog, messagebox
import os

class QGIS_KML_to_DJI_Pilot_2_KML:
    def __init__(self, root):
        self.root = root
        self.root.title("KML Processor")

        self.file_paths = None
        self.output_dir = None

        # Load KML Files Button
        self.load_files_button = tk.Button(root, text="Load KML Files", command=self.load_kml_files)
        self.load_files_button.pack(pady=10)

        self.files_label = tk.Label(root, text="No KML files loaded")
        self.files_label.pack()

        # Process Button
        self.process_button = tk.Button(root, text="Process and Save KML Files", command=self.process_files)
        self.process_button.pack(pady=10)

        # Progress Label
        self.progress_label = tk.Label(root, text="Waiting to start process...")
        self.progress_label.pack(pady=10)

        # Done Button
        self.done_button = tk.Button(root, text="Done", command=self.done)
        self.done_button.pack(pady=10)

    def load_kml_files(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("KML files", "*.kml")])
        if file_paths:
            self.file_paths = file_paths
            self.files_label.config(text=f"{len(file_paths)} KML file(s) loaded")
        else:
            messagebox.showerror("Error", "No files loaded")

    def process_files(self):
        if not self.file_paths:
            messagebox.showerror("Error", "Please load KML files before processing.")
            return

        # Select output folder
        output_dir = filedialog.askdirectory(title='Select Output Directory')
        if not output_dir:
            messagebox.showerror("Error", "No output directory selected")
            return
        else:
            self.output_dir = output_dir

        self.progress_label.config(text="Processing...")
        self.root.update_idletasks()

        for input_file_path in self.file_paths:
            try:
                # Load and parse input KML file
                tree = ET.parse(input_file_path)
                root_element = tree.getroot()

                # Extract the namespace from the root element
                ns = {'kml': 'http://www.opengis.net/kml/2.2'}

                # Find coordinates element in input
                coordinates = root_element.find('.//kml:coordinates', ns)

                if coordinates is None:
                    messagebox.showwarning("Warning", f"No coordinates found in {os.path.basename(input_file_path)}. Skipping.")
                    continue

                # Create output KML file structure
                kml = ET.Element('kml', {'xmlns': 'http://www.opengis.net/kml/2.2'})
                doc = ET.SubElement(kml, 'Document')

                style = ET.SubElement(doc, 'Style', {'id': 'transBluePoly'})
                line_style = ET.SubElement(style, 'LineStyle')
                ET.SubElement(line_style, 'width').text = '1.5'
                poly_style = ET.SubElement(style, 'PolyStyle')
                ET.SubElement(poly_style, 'color').text = '7dff0000'

                placemark = ET.SubElement(doc, 'Placemark')
                ET.SubElement(placemark, 'name').text = 'QGISexport'
                ET.SubElement(placemark, 'styleUrl').text = '#transBluePoly'

                polygon = ET.SubElement(placemark, 'Polygon')
                ET.SubElement(polygon, 'extrude').text = '1'
                ET.SubElement(polygon, 'altitudeMode').text = 'relativeToGround'
                outer_boundary = ET.SubElement(polygon, 'outerBoundaryIs')
                linear_ring = ET.SubElement(outer_boundary, 'LinearRing')

                # Copy the coordinates from the input file to the output file
                # Create a new 'coordinates' element with the same text
                new_coordinates = ET.SubElement(linear_ring, 'coordinates')
                new_coordinates.text = coordinates.text

                # Generate output file name from input file name
                base_name = os.path.basename(input_file_path)
                base_name_without_ext = os.path.splitext(base_name)[0]
                output_file_name = f"{base_name_without_ext}_flightpath.kml"
                output_file_path = os.path.join(self.output_dir, output_file_name)

                # Write KML file
                output_tree = ET.ElementTree(kml)
                output_tree.write(output_file_path, encoding='utf-8', xml_declaration=True)

                self.progress_label.config(text=f"Processed {base_name}")
                self.root.update_idletasks()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while processing {os.path.basename(input_file_path)}: {e}")
                continue

        self.progress_label.config(text="Processing completed.")
        messagebox.showinfo("Info", "All files have been processed successfully.")

    def done(self):
        self.root.quit()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QGIS_KML_to_DJI_Pilot_2_KML(root)
    root.mainloop()
