def generate_explanation(score, features):
    blur = features["blur"]
    brightness = features["brightness"]
    contrast = features["contrast"]

    explanation = []

    # Brightness
    if brightness < 50:
        explanation.append("The image is quite dark (low brightness).")
    elif brightness > 180:
        explanation.append("The image is overexposed (too bright).")
    else:
        explanation.append("The brightness level is acceptable.")

    # Contrast
    if contrast < 30:
        explanation.append("The image has low contrast, making details less distinguishable.")
    else:
        explanation.append("The contrast level is good.")

    # Blur
    if blur < 100:
        explanation.append("The image appears blurry.")
    else:
        explanation.append("The image is relatively sharp.")

    # Final summary
    if score < 40:
        explanation.append("Overall, the image quality is poor and needs improvement.")
    elif score < 70:
        explanation.append("Overall, the image quality is moderate but can be improved.")
    else:
        explanation.append("Overall, the image quality is high and visually appealing.")

    return " ".join(explanation)