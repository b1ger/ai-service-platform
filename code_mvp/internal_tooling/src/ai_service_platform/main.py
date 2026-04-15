import argparse
import sys

from ai_service_platform.utils.io import read_file, write_file
from ai_service_platform.artifacts.intake_processor import process_intake, render_intake_markdown
from ai_service_platform.artifacts.workflow_generator import generate_workflow, render_workflow_markdown
from ai_service_platform.artifacts.proposal_generator import generate_proposal, render_proposal_markdown
from ai_service_platform.artifacts.delivery_pack_builder import build_delivery_pack, render_delivery_markdown

def main():
    parser = argparse.ArgumentParser(description="AI Service Platform Internal Tooling MVP")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Intake command
    intake_parser = subparsers.add_parser("intake", help="Generate an intake summary from raw notes")
    intake_parser.add_argument("--input", required=True, help="Path to raw intake text file")
    intake_parser.add_argument("--segment", required=True, choices=["contractor", "furniture", "clinic"], help="Target client segment")
    intake_parser.add_argument("--output", required=True, help="Destination path for markdown output")

    # Workflow command
    workflow_parser = subparsers.add_parser("workflow", help="Generate a structured workflow map from notes")
    workflow_parser.add_argument("--input", required=True, help="Path to raw workflow notes text file")
    workflow_parser.add_argument("--name", required=True, help="Name of the workflow")
    workflow_parser.add_argument("--segment", required=True, help="Target client segment")
    workflow_parser.add_argument("--output", required=True, help="Destination path for markdown output")

    # Proposal command
    proposal_parser = subparsers.add_parser("proposal", help="Generate a pilot proposal draft from a discovery summary")
    proposal_parser.add_argument("--input", required=True, help="Path to structured discovery summary markdown")
    proposal_parser.add_argument("--name", required=True, help="Name of the proposed pilot workflow")
    proposal_parser.add_argument("--output", required=True, help="Destination path for markdown output")

    # Delivery command
    delivery_parser = subparsers.add_parser("delivery", help="Generate a client-facing delivery pack")
    delivery_parser.add_argument("--workflow", required=True, help="Path to the finalized workflow map markdown")
    delivery_parser.add_argument("--notes", required=True, help="Path to raw delivery notes text file")
    delivery_parser.add_argument("--output", required=True, help="Destination path for markdown output")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    try:
        if args.command == "intake":
            raw_text = read_file(args.input)
            result = process_intake(raw_text, args.segment)
            output_md = render_intake_markdown(result)
            write_file(args.output, output_md)
            print(f"Intake summary generated: {args.output}")

        elif args.command == "workflow":
            notes = read_file(args.input)
            result = generate_workflow(notes, args.name, args.segment)
            output_md = render_workflow_markdown(result)
            write_file(args.output, output_md)
            print(f"Workflow map generated: {args.output}")

        elif args.command == "proposal":
            discovery = read_file(args.input)
            result = generate_proposal(discovery, args.name)
            output_md = render_proposal_markdown(result)
            write_file(args.output, output_md)
            print(f"Proposal draft generated: {args.output}")

        elif args.command == "delivery":
            workflow_text = read_file(args.workflow)
            notes_text = read_file(args.notes)
            result = build_delivery_pack(workflow_text, notes_text)
            output_md = render_delivery_markdown(result)
            write_file(args.output, output_md)
            print(f"Delivery pack generated: {args.output}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
