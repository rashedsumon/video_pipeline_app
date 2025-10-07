import os
import subprocess

def reassemble_video(frames, meta):
    out_path = os.path.join("outputs", "reassembled_" + os.path.basename(meta["path"]))
    # Assume frames are saved in temp folder as frame_001.png ...
    frame_folder = "temp_frames"
    # ffmpeg command
    cmd = [
        "ffmpeg", "-y",
        "-framerate", str(meta["fps"]),
        "-i", os.path.join(frame_folder, "frame_%03d.png"),
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        out_path
    ]
    subprocess.run(cmd, check=True)
    return out_path
