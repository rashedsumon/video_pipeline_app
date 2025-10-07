import streamlit as st
from pipeline.ingest import load_videos
from pipeline.slicer import slice_video
from pipeline.ai_generator import generate_frames
from pipeline.enhancement import enhance_frames
from pipeline.reassembly import reassemble_video
from pipeline.post_processing import add_metadata_and_branding

st.set_page_config(page_title="AI Video Replication Pipeline", layout="wide")
st.title("Automated AI Video Replication Pipeline")

video_files = st.file_uploader("Upload Videos or select Kaggle sample", type=["mp4", "mov"], accept_multiple_files=True)

if st.button("Run Pipeline"):
    if not video_files:
        st.warning("Please upload at least one video or mount the Kaggle dataset.")
    else:
        for vid in video_files:
            st.info(f"Processing video: {vid.name}")

            # Step 1: Ingest & metadata
            meta = load_videos(vid)
            st.write(f"Video metadata: {meta}")

            # Step 2: Slice frames
            slices = slice_video(vid)
            st.write(f"Sliced into {len(slices)} frames/chunks.")

            # Step 3: AI generation/modification
            generated_frames = generate_frames(slices)
            st.write("Frames generated via AI/Sora API.")

            # Step 4: Enhancement / Watermark
            clean_frames = enhance_frames(generated_frames)
            st.write("Frames enhanced and watermarks removed if permitted.")

            # Step 5: Reassembly
            final_video_path = reassemble_video(clean_frames, meta)
            st.write(f"Video reassembled at: {final_video_path}")

            # Step 6: Post-processing
            output_path = add_metadata_and_branding(final_video_path)
            st.success(f"Pipeline completed! Output saved to: {output_path}")
