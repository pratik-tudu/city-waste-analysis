import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt

# ---------- SAMPLE DATA (Fallback) ----------
def load_sample_data():
    data = {
        "Date": [
            "2025-01-01","2025-01-02","2025-01-03","2025-01-04",
            "2025-01-05","2025-01-06","2025-01-07"
        ] * 4,

        "Zone": ["North"]*7 + ["South"]*7 + ["East"]*7 + ["West"]*7,

        "Area": (
            ["Green Park", "Lake View", "River Side", "Hill Town",
             "Green Park", "Lake View", "River Side"] * 4
        ),

        "Waste_Type": (
            ["Organic", "Plastic", "Organic", "Plastic",
             "Organic", "Plastic", "Organic"] * 4
        ),

        "Waste_Collected_Tons": [
            20, 15, 18, 12, 25, 14, 22,
            17, 13, 19, 11, 23, 16, 21,
            14, 10, 16, 9, 18, 12, 17,
            16, 11, 20, 13, 22, 15, 19
        ]
    }

    return pd.DataFrame(data)


# ---------- MAIN FUNCTION ----------
def process_csv(file):
    try:
        if file is not None:
            df = pd.read_csv(file.name)
        else:
            df = load_sample_data()

        # Zone-wise aggregation
        zone_wise = df.groupby("Zone")["Waste_Collected_Tons"].sum()

        # Plot
        fig, ax = plt.subplots()
        zone_wise.plot(kind="bar", ax=ax)
        ax.set_title("Zone-wise Waste Collection")
        ax.set_ylabel("Waste Collected (Tons)")
        plt.tight_layout()

        return df, fig

    except Exception as e:
        return pd.DataFrame({"Error": [str(e)]}), None

# ---------- GRADIO UI ----------
with gr.Blocks() as demo:
    gr.Markdown("## 🗑️ City Waste Collection Dashboard")
    gr.Markdown("Upload a CSV file or use sample data")

    file_input = gr.File(label="Upload CSV File", file_types=[".csv"])
    btn = gr.Button("Analyze Data")

    data_output = gr.Dataframe(label="Dataset")
    plot_output = gr.Plot(label="Zone-wise Waste Collection")

    btn.click(
        fn=process_csv,
        inputs=file_input,
        outputs=[data_output, plot_output]
    )

if __name__ == "__main__":
    demo.launch(ssr_mode=False)

