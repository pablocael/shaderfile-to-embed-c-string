# shaderfile-to-embed-c-string
Converts a Shader file into a C++ / C string that can be embed into a C or C++ program.

# Dependencies
## argparse
python -m pip install argparse


# Usage Example
python convert_shader_to_c_string --input=myshader.vert

or 

python convert_shader_to_c_string --input=myshader.vert > output.txt
