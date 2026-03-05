from backend.video_processor import process_video
from backend.visual_analyzer import analyze_frames
from backend.audio_analyzer import analyze_audio
from backend.nlp_analyzer import transcribe_audio, analyze_nlp
from backend.feature_engineering import (
    normalize_audio_metrics,
    normalize_visual_metrics,
    normalize_nlp_metrics
)
from backend.scorer import evaluation
import json
    

def run_pipeline(video_name, progress_callback=None):
    """
    Runs full SpeakSense AI pipeline.
    Returns final_result dictionary.
    Callbacks for progress bar updation.
    """

    # Extract audio and frames
    if progress_callback:
        progress_callback(10, "Processing Video...")
    result = process_video(video_name)
    frame_path = result["frames_path"]


    # Visual metrics
    if progress_callback:
        progress_callback(25, "Analyzing visual features...")
    visual_metrics = analyze_frames(frame_path)


    # Speech-to-text
    if progress_callback:
        progress_callback(45, "Transcribing audio...")
    text = transcribe_audio(video_name)


    # Audio metrics
    if progress_callback:
        progress_callback(60, "Analyzing audio metrics...")
    audio_metrics = analyze_audio(video_name, text)


    # NLP metrics
    if progress_callback:
        progress_callback(70, "Running NLP analytics...")
    duration_seconds = audio_metrics["duration_seconds"]
    nlp_metrics = analyze_nlp(text, duration_seconds)


     # Normalize
    visual_scores = normalize_visual_metrics(visual_metrics)
    audio_scores = normalize_audio_metrics(audio_metrics)
    nlp_scores = normalize_nlp_metrics(nlp_metrics)


    # Final evaluation
    final_result = evaluation(
        visual_scores,
        audio_scores,
        nlp_scores
    )
    if progress_callback:
        progress_callback(100, "Analysis Complete ✔️")

    return final_result



if __name__ == "__main__":

    video_name = input("Enter filename: ").strip()

    final_result = run_pipeline(video_name)

    print("\nFinal Result:\n")
    print(json.dumps(final_result, indent=4))