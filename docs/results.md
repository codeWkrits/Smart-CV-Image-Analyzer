# Results and Demonstration

For a typical sample image containing simple geometric objects, the application produces:

- an edge-detection image;
- a shape-annotated image;
- a face-detection image; and
- a JSON report containing image properties and detection counts.

The CLI prints a completion message and the output directory. The project also includes automated tests for image analysis, preprocessing output, and contour classification.

## Example Commands
```text
python main.py image --input input/sample.ppm --output output
python main.py preprocess --input input/sample.ppm --operation edges --output output/edges.jpg
python main.py shapes --input input/sample.ppm --output output/shapes.jpg
python main.py detect --input input/sample.ppm --output output/detected.jpg
```
