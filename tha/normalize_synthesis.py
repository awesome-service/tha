from khmercut import tokenize

import tha.normalize
import tha.phone_numbers
import tha.urls
import tha.datetime
import tha.hashtags
import tha.ascii_lines
import tha.license_plate
import tha.cardinals
import tha.decimals
import tha.ordinals
import tha.currency
import tha.parenthesis
import tha.repeater
import tha.quotings
import tha.punctuations

def normalize_synthesis(text: str) -> str:
    processors = [
        tha.normalize.processor,
        tha.phone_numbers.processor,
        tha.urls.processor,
        tha.datetime.time_processor,
        tha.datetime.date_processor,
        tha.hashtags.processor,
        tha.ascii_lines.processor,
        tha.license_plate.processor,
        tha.decimals.processor,
        tha.ordinals.processor,
        tha.currency.processor,
        tha.quotings.processor,
        tha.parenthesis.processor,
    ]
    for processor in processors:
        if processor:
            text = processor(text)
            
    repeater_text =  tha.repeater.processor(text, tokenizer= tokenize)
    punctuations_text = "".join(list(tha.punctuations.processor(repeater_text)))
    return punctuations_text

