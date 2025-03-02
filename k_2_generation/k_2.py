import base64
import openai
import os
from dotenv import load_dotenv

load_dotenv()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# multi-domain example
DOMAIN = "Energy and Climate Science"
K = 2

# example images, captions and combined question
IMAGE_EX1 = r"Charts-20250226T221112Z-001/Charts/242.png"
IMAGE_EX2 = r"Charts-20250226T221112Z-001/Charts/254.png"

CAPTION_EX1 = '''
Figure 11.11. Temperature anomalies with respect to 1901 to 1950 for fi ve North American land regions for 1906 to 2005 (black line) and as simulated (red envelope) by 
MMD models incorporating known forcings; and as projected for 2001 to 2100 by MMD models for the A1B scenario (orange envelope). The bars at the end of the orange enve-
lope represent the range of projected changes for 2091 to 2100 for the B1 scenario (blue), the A1B scenario (orange) and the A2 scenario (red). The black line is dashed where 
observations are present for less than 50% of the area in the decade concerned. More details on the construction of these fi gures are given in Box 11.1 and Section 11.1.2.
'''
CAPTION_EX2 = '''
Figure 10.31. Projected global average sea level rise (m) due to thermal expansion during the 21st century relative to 1980 to 1999 under SRES scenarios A1B, A2 and B1. 
See Table 8.1 for model descriptions.
'''
QUESTION = '''
How do the projected temperature anomalies for the 21st century for scenarios A1B, A2, and B1 contribute to the thermal expansion of the ocean, which in turn is correlated with the projected global average sea level rise? Based on the figures, explain the relationship between these temperature anomalies and thermal expansion, and assess whether the data provided is sufficient to establish a direct quantitative correlation, and if not a degree of confidence for claiming a correlation.
'''

# testing images and captions
IMAGE1 = r"Charts-20250226T221112Z-001/Charts/276.png" #297
IMAGE2 = r"Charts-20250226T221112Z-001/Charts/297.png" #276
CAPTION1 = '''
Figure 9.30: Storm track activity averaged over north-west Europe
(6oW to 20oE, 40o to 70oN) in the ECHAM4/OPYC greenhouse gas
scenario run (Unit: gpm). A 4-year running mean is shown for smoother
display. The grey band indicates the variability of this index in the
control run as measured by one standard deviation. The non-linear
climate trend optimally obtained from quadratic curve fitting is marked
by the dashed line; y-axis is activity in gpm (geopotential metres) and
x-axis is time in calendar years. From Ulbrich and Christoph (1999).
'''
CAPTION2 = '''
Figure 10.15. Evolution of the Atlantic meridional overturning circulation (MOC) at 30degN in simulations with the suite of comprehensive coupled climate models (see Table 8.1 
for model details) from 1850 to 2100 using 20th Century Climate in Coupled Models (20C3M) simulations for 1850 to 1999 and the SRES A1B emissions scenario for 1999 to 
2100. Some of the models continue the integration to year 2200 with the forcing held constant at the values of year 2100. Observationally based estimates of late-20th century 
MOC are shown as vertical bars on the left. Three simulations show a steady or rapid slow down of the MOC that is unrelated to the forcing; a few others have late-20th century 
simulated values that are inconsistent with observational estimates. Of the model simulations consistent with the late-20th century observational estimates, no simulation 
shows an increase in the MOC during the 21st century; reductions range from indistinguishable within the simulated natural variability to over 50% relative to the 1960 to 1990 
mean; and none of the models projects an abrupt transition to an off state of the MOC. Adapted from Schmittner et al. (2005) with additions.
'''

# encode images into base64
im_ex1 = encode_image(IMAGE_EX1)
im_ex2 = encode_image(IMAGE_EX2)
im_1 = encode_image(IMAGE1)
im_2 = encode_image(IMAGE2)

with open("prompts/generation/input_prompt.txt", "r") as f:
    prompt_ex = f.read()

prompt1 = prompt_ex.format(
    DOMAIN=DOMAIN,
    K=K,
    IMAGE_EX1=im_ex1,
    CAPTION_EX1=CAPTION_EX1,
    IMAGE_EX2=im_ex2,
    CAPTION_EX2=CAPTION_EX2,
    QUESTION_EX1 = QUESTION,
    IMAGE1=im_1,
    CAPTION1=CAPTION1,
    IMAGE2=im_2,
    CAPTION2=CAPTION2
)

openai.api_key = os.getenv("OPEN_AI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-4-turbo",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": prompt1},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{im_ex1}"}},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{im_ex2}"}},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{im_1}"}},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{im_2}"}}
        ]
    }]
)

print(response["choices"][0]["message"]["content"])