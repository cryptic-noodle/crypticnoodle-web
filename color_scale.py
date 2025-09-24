def dim_color(ref_dim,rgb=(247, 241, 255), ref_bright=(255, 255, 255)):
    """
    Dim an RGB color using the same brightness scaling factor
    as ref_bright -> ref_dim.

    Args:
        rgb (tuple): (R, G, B) values of the color to dim.
        ref_bright (tuple): Reference bright color (default white).
        ref_dim (tuple): Reference dimmed color.

    Returns:
        tuple: Dimmed (R, G, B).
    """
    # Calculate average brightness of reference colors
    bright_avg = sum(ref_bright) / 3
    dim_avg = sum(ref_dim) / 3
    
    # Scale factor
    scale = dim_avg / bright_avg
    
    # Apply scaling
    return tuple(max(0, min(255, round(c * scale))) for c in rgb)


# Example usage:
print(dim_color((250, 250, 250)))
print(dim_color((228, 228, 231)))
print(dim_color((212, 212, 216)))  # → (207, 202, 213)
print(dim_color((161, 161, 170)))  # → (191, 191, 193)
print(dim_color((113, 113, 122)))  # → (145, 141, 150)
print(dim_color((82, 82, 91)))  # → (95, 95, 102)
