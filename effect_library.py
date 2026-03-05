def build_speed_ramp_filter(input_label: str, output_label: str, speed: float = 2.0) -> str:
    """Returns FFmpeg filter string for speed ramp."""
    return f"[{input_label}]setpts={1/speed}*PTS[{output_label}];"

def build_glow_filter(input_label: str, output_label: str) -> str:
    """Glow effect using boxblur + overlay."""
    return (f"[{input_label}]split[{input_label}A][{input_label}B];"
            f"[{input_label}B]boxblur=10:5[blur];"
            f"[{input_label}A][blur]overlay[{output_label}];")

# ... 100+ such functions
