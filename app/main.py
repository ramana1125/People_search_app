from app.rag_pipeline import run_search
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="People Search CLI")
    parser.add_argument("--query", type=str, required=True, help="Search query")
    parser.add_argument("--top_k", type=int, default=5, help="Number of profiles")
    args = parser.parse_args()

    print("🔍 Running search...")
    results = run_search(args.query, top_k=args.top_k)

    print("\n📌 Top Results:")
    if not results:
        print("No matching profiles found.")
    else:
        for i, res in enumerate(results, start=1):
            p = res["profile"]
            print(f"\nResult {i}:")
            print(f"Name: {p.get('name')}")
            print(f"Location: {p.get('location')}")
            print(f"Interests: {p.get('interests')}")
            print(f"Bio: {p.get('bio')}")
            print(f"Compatibility: {res['compatibility']}%")
            print(f"Insights: {res['insights']}")
