# render
Render from scratch.

[Click here for example.](./renders)

## Files

### Functionals

- render.py

- operations.py / operations_cython.pyx

### Examples

- example.py

- example_pre_render.py

## Formulas

### Main formula of reflection and refraction of light used

- `intensity`: Light intensity.
- `exposition`: Light exposure.
- `polygon_normalized[i]`: Normalized vector of the polygon at index `i`.
- `polygon.rough`: Polygon roughness.
- `polygon.reflection`: Polygon reflection.
- `polygon.dispersion_light`: Polygon light dispersion.
- `light_normalized[i]`: Normalized vector of the light at index `i`.
- `polygon.metalic`: Polygon metallicity.
- `distance`: Distance from the light source to the calculation point.
- `light.ambient`: Ambient light.

(intensity * (exposition * (polygon_normalized[i] * polygon.rough) + (polygon.reflection + polygon.dispersion_light) * (light_normalized[i] * polygon.metalic)) / distance^(1/2) + light.ambient)


