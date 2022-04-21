## Choices for the Weekly Availability Model
DRAWING = "Drawing"
TATTOOING = "Tattoing"
CONSULATION = "Consultation"
MEETING = "Meeting"
LEARNING = "Learning"
TRAINING = "Training"
MANAGING = "Managing"
CUSTOMER_SERVICE = "Customer Service"
GENERAL = "General"
OTHER = "Other"

AVAILABILITY_TYPES = (
    (DRAWING, "Drawing"),
    (TATTOOING, "Tattoing"),
    (CONSULATION, "Consulation"),
    (MEETING, "Meeting"),
    (LEARNING, "Learning"),
    (MANAGING, "Managing"),
    (CUSTOMER_SERVICE, "Customer Service"),
    (GENERAL, "General"),
    (OTHER, "Other"),
)

MONDAY = "Monday"
TUESDAY = "Tuesday"
WEDNESDAY = "Wednesday"
THURSDAY = "Thursday"
FRIDAY = "Friday"
SATURDAY = "Saturday"
SUNDAY = "Sunday"

DAYS_OF_WEEK = (
    (MONDAY, "Monday"),
    (TUESDAY, "Tuesday"),
    (WEDNESDAY, "Wednesday"),
    (THURSDAY, "Thursday"),
    (FRIDAY, "Friday"),
    (SATURDAY, "Saturday"),
    (SUNDAY, "Sunday"),
)

## Choices for the Consultation Model
BLACK_AND_WHITE = "Black and White"
FULL_COLOR = "Full Color"
OTHER = "Other"

TATTOO_COLOR_CHOICES = (
    (BLACK_AND_WHITE, "Black and White"),
    (FULL_COLOR, "Full Color"),
    (OTHER, "Other"),
)

MORNING = "Morning"
AFTERNOON = "Afternoon"
EVENING = "Evening"

PREFERRED_TIME_OF_DAY = (
    (MORNING, "Morning"),
    (AFTERNOON, "Afternoon"),
    (EVENING, "Evening"),
)

APPROVED = "Approved"
MORE_INFO = "More Info"
SCHEDULED_AND_DEPOST_PAID = "Scheduled and "
REFERRED_TO_ARTIST = "Referred to another Artist"

CONSULT_STATUS_CHOICES = (
    (APPROVED, "Approved"),
    (MORE_INFO, "More Info"),
    (REFERRED_TO_ARTIST, "Referred"),
    (SCHEDULED_AND_DEPOST_PAID, "Scheduled and Deposit Paid")
)

## Choices for Bookings Model
SCHEDULED = "Scheduled"
RESCHEDULED = "Re-scheduled"
CANCELLED = "Cancelled"
COMPLETED = "Completed"

BOOKING_STATUS_CHOICES = (
    (SCHEDULED, "Scheduled"),
    (RESCHEDULED, "Rescheduled"),
    (CANCELLED, "Cancelled"),
    (COMPLETED, "Completed"),
)

## Post Choices
TRADITIONAL = "Traditional"
OLD_SCHOOL = "Old School"
NEO_TRADITIONAL = "Neo-Traditional"
TRIBAL = "Tribal"
WATERCOLOR = "Watercolor"
BLACKWORK = "Blackwork"
REALISM = "Realism"
GEOMETRIC = "Geometric"



POST_CATEGORIES = (
    (TRADITIONAL, "Traditional"),
    (OLD_SCHOOL, "Old School"),
    (NEO_TRADITIONAL, "Neo-Traditional"),
    (TRIBAL, "Tribal"),
    (WATERCOLOR, "Watercolor"),
    (BLACKWORK, "Blackwork"),
    (REALISM, "Realism"),
    (GEOMETRIC, "Geometric"),
)


## Choices for Merch
APPAREL = "Apparel"
PRINTS = "Prints"
DIGITAL_ART = "Digital Art"
STICKER = "Sticker"

MERCH_ITEM_TYPES = (
    (APPAREL, "Apparel"),
    (PRINTS, "Prints"),
    (DIGITAL_ART, "Digital Art"),
    (STICKER, "Sticker"),
)

## Choices for Communication Prefrences

TEXT = "Text"
EMAIL = "Email"

COMMUNICATION_PREFRENCE = (
    (TEXT, "Text"),
    (EMAIL, "Email"),
)

