"""
plot_styles.py — Style definitions for the ICESat-2 Profile Viewer.

Each entry in PLOT_STYLES is a self-contained style spec consumed by
dock_widget.py().  Add or modify entries here to create
new styles without touching the main plugin code.

Keys per style
--------------
fig_facecolor       Figure background colour.
ax_facecolor        Axes background colour.
text_color          Tick labels, axis labels.
title_color         Plot title.
spine_color         Visible spine colour (bottom + left).
grid_color          Grid line colour.
grid_alpha          Grid opacity (0 = no grid).
grid_linestyle      Grid line style ('-', '--', ':', '-.').
tick_labelsize      Tick label font size (pt).
label_fontsize      Axis label font size (pt).
title_fontsize      Title font size (pt).
legend_facecolor    Legend background.
legend_edgecolor    Legend border.
legend_labelcolor   Legend text.
legend_framealpha   Legend background opacity.
water_fill          Colour of the water-region axvspan.
water_fill_alpha    Opacity of the water-region axvspan.
water_edge          Edge colour of the water-point diamond markers.
font_family         Matplotlib font family string, or None for default.
rcparams            Dict of extra matplotlib rcParam overrides applied
                    via rc_context() for the duration of a single draw.
conf_colors         (optional) Override the default confidence colour map.
                    Keys are integer confidence values (-1 … 4).
overlay_palette     (optional) Override the default overlay line colours.
                    Cycled when more overlays are added than palette entries.

Author: H.B. Rotteveel
Date: 29/04/2026
"""


# Default confidence colour map and labels
CONF_COLORS = {
    -1: "#9e9e9e",
     0: "#e0e0e0",
     1: "#ffeb3b",
     2: "#ff9800",
     3: "#4caf50",
     4: "#00bcd4",
}

CONF_LABELS = {
    -1: "-1  invalid",
     0:  "0  noise",
     1:  "1  low",
     2:  "2  medium",
     3:  "3  high",
     4:  "4  very high",
}

# Default overlay line palette
OVERLAY_PALETTE = [
    "#ff6b6b", "#ffd93d", "#6bcb77", "#4d96ff",
    "#f08cff", "#ff9f43", "#48dbfb", "#ff9ff3",
]


# Plot styles
PLOT_STYLES = {
    "Default (dark)": {
        "fig_facecolor":     "#12121f",
        "ax_facecolor":      "#1a1a2e",
        "text_color":        "#cccccc",
        "title_color":       "#ffffff",
        "spine_color":       "#555555",
        "grid_color":        "#555555",
        "grid_alpha":        0.35,
        "grid_linestyle":    "--",
        "tick_labelsize":    8,
        "label_fontsize":    9,
        "title_fontsize":    10,
        "legend_facecolor":  "#1e1e3a",
        "legend_edgecolor":  "#444444",
        "legend_labelcolor": "#dddddd",
        "legend_framealpha": 0.65,
        "water_fill":        "#1a6fa8",
        "water_fill_alpha":  0.18,
        "water_edge":        "#7ecfff",
        "font_family":       None,
        "rcparams":          {},
    },

    "Academic paper": {
        "fig_facecolor":     "white",
        "ax_facecolor":      "white",
        "text_color":        "black",
        "title_color":       "black",
        "spine_color":       "black",
        "grid_color":        "black",
        "grid_alpha":        0.15,
        "grid_linestyle":    ":",
        "tick_labelsize":    9,
        "label_fontsize":    10,
        "title_fontsize":    11,
        "legend_facecolor":  "white",
        "legend_edgecolor":  "black",
        "legend_labelcolor": "black",
        "legend_framealpha": 1.0,
        "water_fill":        "#4393c3",
        "water_fill_alpha":  0.20,
        "water_edge":        "#2166ac",
        "font_family":       "serif",
        "rcparams": {
            "font.family":         "serif",
            "axes.linewidth":      0.8,
            "xtick.direction":     "in",
            "ytick.direction":     "in",
            "xtick.major.width":   0.8,
            "ytick.major.width":   0.8,
            "xtick.minor.visible": True,
            "ytick.minor.visible": True,
            "xtick.minor.width":   0.6,
            "ytick.minor.width":   0.6,
        },
        # Colourblind-friendly sequential palette (print-safe on white).
        "conf_colors": {
            -1: "#bdbdbd",
             0: "#d9d9d9",
             1: "#fdcc8a",
             2: "#fc8d59",
             3: "#e34a33",
             4: "#b30000",
        },
        # Overlay colours distinguishable in greyscale.
        "overlay_palette": [
            "#1b7837", "#762a83", "#c51b7d",
            "#d6604d", "#4393c3", "#878787",
        ],
    },

    "Presentation (light)": {
        "fig_facecolor":     "white",
        "ax_facecolor":      "white",
        "text_color":        "#333333",
        "title_color":       "#111111",
        "spine_color":       "#aaaaaa",
        "grid_color":        "#cccccc",
        "grid_alpha":        0.60,
        "grid_linestyle":    "-",
        "tick_labelsize":    11,
        "label_fontsize":    12,
        "title_fontsize":    13,
        "legend_facecolor":  "#ffffff",
        "legend_edgecolor":  "#cccccc",
        "legend_labelcolor": "#333333",
        "legend_framealpha": 0.80,
        "water_fill":        "#1a78c2",
        "water_fill_alpha":  0.15,
        "water_edge":        "#1a78c2",
        "font_family":       "sans-serif",
        "rcparams":          {},
    },

    "Minimal (no grid)": {
        "fig_facecolor":     "white",
        "ax_facecolor":      "white",
        "text_color":        "#222222",
        "title_color":       "#111111",
        "spine_color":       "#333333",
        "grid_color":        "black",
        "grid_alpha":        0.0,
        "grid_linestyle":    "-",
        "tick_labelsize":    9,
        "label_fontsize":    10,
        "title_fontsize":    11,
        "legend_facecolor":  "white",
        "legend_edgecolor":  "#333333",
        "legend_labelcolor": "#222222",
        "legend_framealpha": 1.0,
        "water_fill":        "#6baed6",
        "water_fill_alpha":  0.25,
        "water_edge":        "#2171b5",
        "font_family":       "sans-serif",
        "rcparams": {
            "axes.spines.top":   False,
            "axes.spines.right": False,
        },
    },
}

# Keys required in every style block loaded from a text file
_REQUIRED_KEYS = {
    "fig_facecolor", "ax_facecolor", "text_color", "title_color",
    "spine_color", "grid_color", "grid_alpha", "grid_linestyle",
    "tick_labelsize", "label_fontsize", "title_fontsize",
    "legend_facecolor", "legend_edgecolor", "legend_labelcolor",
    "legend_framealpha", "water_fill", "water_fill_alpha", "water_edge",
    "font_family",
}

# Keys whose values must be cast to float
_FLOAT_KEYS = {
    "grid_alpha", "legend_framealpha", "water_fill_alpha",
    "tick_labelsize", "label_fontsize", "title_fontsize",
}

# Text-file parser
def _cast_value(key, raw):
    """
    Convert a raw string value to the correct Python type for *key*.

    Rules applied in order:
      1. Float keys (grid_alpha, font sizes, …)  -> float
      2. "none"                                   -> None  (font_family)
      3. "true" / "false"                         -> bool  (rcparams flags)
      4. Bare integer                             -> int
      5. Bare float                               -> float
      6. Anything else                            -> str as-is
    """
    stripped = raw.strip()

    if key in _FLOAT_KEYS:
        return float(stripped)

    low = stripped.lower()
    if low == "none":
        return None
    if low == "true":
        return True
    if low == "false":
        return False

    try:
        return int(stripped)
    except ValueError:
        pass
    try:
        return float(stripped)
    except ValueError:
        pass

    return stripped


def load_styles_from_file(path):
    """
    Parse a style definition text file and return a dict of style dicts.

    File format (see style_template.txt for a full annotated example)
    ------------------------------------------------------------------
    - Lines starting with '#' are comments; blank lines are ignored.
    - '[Style Name]'                 opens a main style block.
    - '[Style Name.rcparams]'        opens an rcparams sub-block.
    - '[Style Name.conf_colors]'     opens a conf_colors sub-block.
    - '[Style Name.overlay_palette]' opens an overlay_palette sub-block.
    - Inside main / rcparams / conf_colors blocks: key = value
    - Inside overlay_palette blocks: one hex colour per line.

    Parameters
    ----------
    path : str
        Absolute path to the style file.

    Returns
    -------
    dict
        {style_name: style_dict, ...} ready to merge into PLOT_STYLES.

    Raises
    ------
    ValueError
        If a style block is missing required keys, or a value cannot be
        cast to the expected type.
    OSError
        If the file cannot be opened.
    """
    styles = {}  # name -> partially built dict
    rcparams = {}  # name -> {rcparam_key: value}
    conf_colors = {}  # name -> {int_key: colour_str}
    ov_palettes = {}  # name -> [colour_str, ...]

    current_style = None  # name of the style being parsed
    current_section = None  # "main" | "rcparams" | "conf_colors" | "overlay_palette"

    with open(path, encoding="utf-8") as fh:
        for lineno, raw_line in enumerate(fh, start=1):
            line = raw_line.strip()

            # Skip blanks and comments
            if not line or line.startswith("#"):
                continue

            # Section header
            if line.startswith("[") and line.endswith("]"):
                header = line[1:-1].strip()

                if header.endswith(".rcparams"):
                    parent = header[: -len(".rcparams")].strip()
                    current_style = parent
                    current_section = "rcparams"
                    rcparams.setdefault(parent, {})

                elif header.endswith(".conf_colors"):
                    parent = header[: -len(".conf_colors")].strip()
                    current_style = parent
                    current_section = "conf_colors"
                    conf_colors.setdefault(parent, {})

                elif header.endswith(".overlay_palette"):
                    parent = header[: -len(".overlay_palette")].strip()
                    current_style = parent
                    current_section = "overlay_palette"
                    ov_palettes.setdefault(parent, [])

                else:
                    current_style = header
                    current_section = "main"
                    styles[current_style] = {}

                continue

            # Content line — must belong to an open section
            if current_style is None:
                raise ValueError(
                    f"Line {lineno}: content found outside a style block: {raw_line!r}"
                )

            # overlay_palette: one colour per non-blank, non-comment line
            if current_section == "overlay_palette":
                # Strip a leading '#' to test for hex, then restore it
                candidate = line.lstrip("#")
                if all(c in "0123456789abcdefABCDEF" for c in candidate) \
                        and len(candidate) in (3, 6, 8):
                    line = "#" + candidate
                ov_palettes[current_style].append(line)
                continue

            # key = value lines (main, rcparams, conf_colors)
            if "=" not in line:
                raise ValueError(
                    f"Line {lineno}: expected 'key = value', got: {raw_line!r}"
                )

            key, _, raw_val = line.partition("=")
            key = key.strip()
            raw_val = raw_val.strip()

            if current_section == "main":
                styles[current_style][key] = _cast_value(key, raw_val)

            elif current_section == "rcparams":
                rcparams[current_style][key] = _cast_value(key, raw_val)

            elif current_section == "conf_colors":
                try:
                    int_key = int(key)
                except ValueError:
                    raise ValueError(
                        f"Line {lineno}: conf_colors key must be an integer, "
                        f"got {key!r}"
                    )
                conf_colors[current_style][int_key] = raw_val

    # Validate and assemble each style
    result = {}
    for name, spec in styles.items():
        missing = _REQUIRED_KEYS - spec.keys()
        if missing:
            raise ValueError(
                f"Style '{name}' is missing required keys: {sorted(missing)}"
            )

        spec["rcparams"] = rcparams.get(name, {})
        if name in conf_colors:
            spec["conf_colors"] = conf_colors[name]
        if name in ov_palettes and ov_palettes[name]:
            spec["overlay_palette"] = ov_palettes[name]

        result[name] = spec

    return result