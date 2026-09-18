import argparse
from pathlib import Path

from src.preprocessing import preprocess_image
from src.object_detection import detect_faces
from src.shape_detection import detect_shapes
from src.image_analysis import analyze_image
from src.video_analysis import analyze_video_motion
from src.report_generator import save_report


def require_file(path):
    file_path = Path(path)
    if not file_path.is_file():
        raise FileNotFoundError(f"Input file not found: {file_path}")
    return str(file_path)


def build_parser():
    parser = argparse.ArgumentParser(description="Smart Computer Vision Image Analyzer")
    sub = parser.add_subparsers(dest="command", required=True)

    image = sub.add_parser("image", help="Run complete image analysis")
    image.add_argument("--input", required=True)
    image.add_argument("--output", default="output")

    prep = sub.add_parser("preprocess", help="Run image preprocessing")
    prep.add_argument("--input", required=True)
    prep.add_argument("--operation", choices=["resize", "gray", "blur", "threshold", "edges"], required=True)
    prep.add_argument("--output", required=True)

    shapes = sub.add_parser("shapes", help="Detect geometric shapes")
    shapes.add_argument("--input", required=True)
    shapes.add_argument("--output", required=True)

    detect = sub.add_parser("detect", help="Detect faces")
    detect.add_argument("--input", required=True)
    detect.add_argument("--output", required=True)

    video = sub.add_parser("video", help="Detect motion in video")
    video.add_argument("--input", required=True)
    video.add_argument("--output", required=True)
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    try:
        source = require_file(args.input)
        if args.command == "image":
            output = Path(args.output)
            output.mkdir(parents=True, exist_ok=True)
            report = analyze_image(source)
            preprocess_image(source, output / "edges.jpg", "edges")
            shapes = detect_shapes(source, output / "shapes.jpg")
            faces = detect_faces(source, output / "detected.jpg")
            report.update({"shape_contours": shapes, "faces_detected": faces})
            save_report(report, output / "analysis_report.json")
            print(f"Analysis complete. Results saved to {output}")
        elif args.command == "preprocess":
            preprocess_image(source, args.output, args.operation)
            print(f"Saved: {args.output}")
        elif args.command == "shapes":
            print(f"Detected shape regions: {detect_shapes(source, args.output)}")
        elif args.command == "detect":
            print(f"Detected faces: {detect_faces(source, args.output)}")
        elif args.command == "video":
            frames, regions = analyze_video_motion(source, args.output)
            print(f"Processed {frames} frames; detected {regions} motion regions.")
    except (FileNotFoundError, ValueError, RuntimeError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
