"""Composer Spike-0 — Gradio demo app.

Run:
    python app.py

Opens http://localhost:7860 with the demo UI.
"""

from pathlib import Path

import gradio as gr
from PIL import Image

from composer import SCENE_PRESETS, generate_composite

ASSETS_INPUTS = Path(__file__).parent / "assets" / "inputs"
ASSETS_OUTPUTS = Path(__file__).parent / "assets" / "outputs"


def run(product_image, scene_label, seed_str):
    if product_image is None:
        return None, None, None, "Завантаж фото продукту, будь ласка."

    # Resolve label → preset key
    preset_key = next(
        (k for k, v in SCENE_PRESETS.items() if v.label == scene_label), None
    )
    if preset_key is None:
        return None, None, None, f"Невідома сцена: {scene_label}"

    seed = None
    if seed_str and seed_str.strip().isdigit():
        seed = int(seed_str.strip())

    try:
        result = generate_composite(
            product_image=product_image,
            scene_key=preset_key,
            seed=seed,
            save_dir=ASSETS_OUTPUTS,
        )
    except Exception as e:
        return None, None, None, f"Помилка: {e}"

    info = (
        f"Готово. Сцена: {scene_label}. "
        f"Продукт збережено піксель-у-піксель — нічого в ньому не регенерувалося. "
        f"Файли збережено в {ASSETS_OUTPUTS.resolve()}."
    )
    return (
        result.product_no_bg,
        result.generated_scene,
        result.final_composite,
        info,
    )


def build_ui() -> gr.Blocks:
    scene_choices = [v.label for v in SCENE_PRESETS.values()]

    with gr.Blocks(
        title="Composer — Spike-0",
        theme=gr.themes.Soft(),
    ) as demo:
        gr.Markdown(
            "# Composer — Spike-0\n"
            "Демо composite-first архітектури. Завантаж реальне фото продукту, "
            "обери сцену, натисни Generate. Продукт залишається незмінним; "
            "фон генерується AI; композиція автоматична."
        )

        with gr.Row():
            with gr.Column(scale=1):
                product_input = gr.Image(
                    label="Реальне фото продукту",
                    type="pil",
                    sources=["upload", "clipboard"],
                )
                scene_dropdown = gr.Dropdown(
                    label="Сцена",
                    choices=scene_choices,
                    value=scene_choices[0],
                )
                seed_input = gr.Textbox(
                    label="Seed (опціонально, для відтворюваних результатів)",
                    placeholder="наприклад: 42",
                )
                generate_btn = gr.Button("Generate", variant="primary")
                status = gr.Markdown()

            with gr.Column(scale=2):
                with gr.Row():
                    product_no_bg = gr.Image(label="1. Продукт без фону", type="pil")
                    scene_img = gr.Image(label="2. Згенерована сцена", type="pil")
                final_img = gr.Image(label="3. Фінальна композиція", type="pil", height=512)

        generate_btn.click(
            run,
            inputs=[product_input, scene_dropdown, seed_input],
            outputs=[product_no_bg, scene_img, final_img, status],
        )

        gr.Markdown(
            "---\n"
            "**Що тут демонструється:** реальне фото продукту йде через rembg "
            "(прибираємо фон), AI генерує нову сцену БЕЗ будь-яких продуктів, "
            "потім продукт композиціонується поверх з тінню. "
            "Жодного разу продукт не передавався diffusion-моделі — "
            "тому упаковка, текст, текстури зберігаються піксель-у-піксель.\n\n"
            "Spike-0 / throwaway code. Production MVP буде окремо."
        )

    return demo


if __name__ == "__main__":
    ASSETS_OUTPUTS.mkdir(parents=True, exist_ok=True)
    build_ui().launch(server_name="127.0.0.1", server_port=7860, inbrowser=True)
