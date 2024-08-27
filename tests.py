from tha.normalize_synthesis import normalize_synthesis
from tha.pronounce import processor as pronounce_processor

TEXT = "តាមរយះ https://google.com 0961231234 ប្រកាស់ថាបានទៅបន្តិចម្ដងៗហើយ មិន\u200bឲ្យ ឃាត់ខ្លួនជនសង្ស័យ០៤នាក់ ករណីលួចខ្សែភ្លើង នៅស្រុកព្រៃនប់ម៉ោង 10:23AM 5th AB 1234 Hello (this will be ignored) world 10:23AM 2024-01-02 ខ្ញុំចូលប្រពេញ។។។។។។"

print("\n# Normalize", normalize_synthesis(TEXT))

OUTPUT = (
  normalize_synthesis(TEXT)
  == "តាមរយះ google dot com សូន្យ▁កៅសិបប្រាំមួយ▁ដប់ពីរ▁សាមសិបមួយ▁ពីររយ▁សាមសិបបួន ប្រកាស់ថាបានទៅបន្តិចម្ដង▁បន្តិចម្ដងហើយ មិនឱ្យ ឃាត់ខ្លួនជនសង្ស័យបួននាក់ ករណីលួចខ្សែភ្លើង នៅស្រុកព្រៃនប់ម៉ោង ដប់ ម្ភៃបី▁A▁M ប្រាំth AB មួយពាន់▁ពីររយ▁សាមសិបបួន Hello world ដប់ ម្ភៃបី▁A▁M ពីរពាន់▁ម្ភៃបួន មួយ ពីរ ខ្ញុំចូលប្រពេញ ។"
)

print("\n# Normalize", OUTPUT)

pronounce_output = pronounce_processor("យោងតាមការសិក្សារបស់ក្រុមហ៊ុន បានឱ្យដឹងថា គម្រោង “ដ៏មហិមា” ")
print("\n# Normalize pronounce", pronounce_output)
