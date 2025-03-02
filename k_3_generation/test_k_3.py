import base64
import openai
import os
from dotenv import load_dotenv
load_dotenv()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    

# Necessary examples for RL
DOMAIN = "Climate Science and Energy"
K = 3

'''
IMAGE_EX1 = "Charts-20250226T221112Z-001\Charts\300.png"
IMAGE_EX2 = "Charts-20250226T221112Z-001\Charts\302.png"
IMAGE_EX3 = "Charts-20250226T221112Z-001\Charts\304.png"
'''

CAPTION_EX1 = '''Figure 3.10 | Probability ratio (PR) of exceeding (heavy precipitation) thresholds. (a) PR of exceeding the 99th (blue) and 99.9th (red) percentile of pre-industrial daily 
precipitation at a given warming level, averaged across land (from Fischer and Knutti, 2015). (b) PR for precipitation extremes (RX1day) for different event probabilities (with RV 
indicating return values) in the current climate (1degC of global warming). Shading shows the interquartile (25-75%) range (from Kharin et al., 2018).
'''
CAPTION_EX2 = '''Figure 1.8: Changes in the temperature of the Northern Hemisphere from surface observations (in red) and from prox-
ies (in black; uncertainty range represented by shading) relative to 1961-1990 average temperature. If this graph were 
plotted relative to 1901-1960 instead of 1961-1990, the temperature changes would be 0.47degF (0.26degC) higher. These 
analyses suggest that current temperatures are higher than seen in the Northern Hemisphere, and likely globally, in at 
least the last 1,700 years, and that the last decade (2006-2015) was the warmest decade on record. (Figure source: 
adapted from Mann et al. 2008193).
'''
CAPTION_EX3 = '''
Figure 3.21 | The dependence of risks and/or impacts associated with the Reasons for Concern (RFCs) on the level of climate change, updated and adapted from WGII AR5 
Ch 19, Figure 19.4 and highlighting the nature of this dependence between 0degC and 2degC warming above pre-industrial levels. As in the AR5, literature was used to make 
expert judgements to assess the levels of global warming at which levels of impact and/or risk are undetectable (white), moderate (yellow), high (red) or very high (purple). 
The colour scheme thus indicates the additional risks due to climate change. The transition from red to purple, introduced for the first time in AR4, is defined by very high risk 
of severe impacts and the presence of significant irreversibility, or persistence of climate-related hazards combined with a limited ability to adapt due to the nature of the 
hazard or impact. Comparison of the increase of risk across RFCs indicates the relative sensitivity of RFCs to increases in GMST. As was done previously, this assessment takes 
autonomous adaptation into account, as well as limits to adaptation (RFC 1, 3, 5) independently of development pathway. The rate and timing of impacts were taken into 
account in assessing RFC 1 and 5. The levels of risk illustrated reflect the judgements of the Ch 3 authors. RFC1 Unique and threatened systems: ecological and human 
systems that have restricted geographic ranges constrained by climate related conditions and have high endemism or other distinctive properties. Examples include coral reefs, 
the Arctic and its indigenous people, mountain glaciers and biodiversity hotspots. RFC2 Extreme weather events: risks/impacts to human health, livelihoods, assets and 
ecosystems from extreme weather events such as heatwaves, heavy rain, drought and associated wildfires, and coastal flooding. RFC3 Distribution of impacts: risks/impacts 
that disproportionately affect particular groups due to uneven distribution of physical climate change hazards, exposure or vulnerability. RFC4 Global aggregate impacts: 
global monetary damage, global scale degradation and loss of ecosystems and biodiversity. RFC5 Large-scale singular events: are relatively large, abrupt and sometimes 
irreversible changes in systems that are caused by global warming. Examples include disintegration of the Greenland and Antarctic ice sheets. The grey bar represents the range 
of GMST for the most recent decade: 2006-2015.
'''

QUESTION = '''
Given the continually rising temperatures since the last 1700 years, how would the risk to RFC1 unique and threatened systems from extreme weather events, such as heavy rainfall and coastal flooding, change/vary in the upcoming decades? Specifically, what % of the overall risk to RFC1 systems is a contribution exceeding precipitation thresholds and the projected impact from increased rising temperatures?
'''

# Actual images and captions for generation
'''
IMAGE1 = "PATH"
IMAGE2 = "PATH"
IMAGE3 = "PATH"
'''

CAPTION1 = '''
Figure ES.3: The two panels above show annual historical and a range of plausible future carbon emissions in
units of gigatons of carbon (GtC) per year (left) and the historical observed and future temperature change that
would result for a range of future scenarios relative to the 1901–1960 average, based on the central estimate (lines)
and a range (shaded areas, two standard deviations) as simulated by the full suite of CMIP5 global climate models
(right). By 2081–2100, the projected range in global mean temperature change is 1.1°–4.3°F under the even lower
scenario (RCP2.6; 0.6°–2.4°C, green), 2.4°–5.9°F under the lower scenario (RCP4.5; 1.3°–3.3°C, blue), 3.0°–6.8°F
under the mid-high scenario (RCP6.0; 1.6°–3.8°C, not shown) and 5.0°–10.2°F under the higher scenario (RCP8.5;
2.8°–5.7°C, orange). See the main report for more details on these scenarios and implications. Based on Figure
4.1 in Chapter 4.
'''
CAPTION2 = '''Figure 4.29: Indicative low(a) and high(b) range estimates of the mitigation potential in the electricity sector based on substitution of existing fossil-fuel thermal power 
stations with nuclear and renewable energy power generation, coupled with energy-efficiency improvements in power-generation plants and transmission, including switching 
from coal to gas and the uptake of CCS. CHP and heat are not included, nor electricity savings from energy-efficiency measures in the building and industry sectors. 
'''
CAPTION3 = '''Figure 4.30: Potential increased emissions from the greater uptake of unconven-
tional oils by 2030 could offset potential reductions from both biofuels and vehicle-
efficiency improvements, but will be subject to the future availability and price of 
conventional oil.
'''

'''
im_ex1 = encode_image(IMAGE_EX1)
im_ex2 = encode_image(IMAGE_EX2)
im_ex3 = encode_image(IMAGE_EX3)
im_1 = encode_image(IMAGE1)
im_2 = encode_image(IMAGE2)
im_3 = encode_image(IMAGE3)
'''

with open("prompts/generation/test_prompt.txt", "r") as f:
    prompt_ex = f.read()

prompt1 = prompt_ex.format(
    DOMAIN=DOMAIN,
    K=K,
    QUESTION_EX1 = QUESTION,
    CAPTION1=CAPTION1,
    CAPTION2=CAPTION2,
    CAPTION3=CAPTION3
)

openai.api_key = os.getenv("OPEN_AI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": prompt1},
        ]
    }]
)

print(response["choices"][0]["message"]["content"])