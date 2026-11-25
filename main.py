import os

LINE = "Our open-plan office was built for collaboration, so now the whole team collaborates on finding somewhere quiet to work."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
