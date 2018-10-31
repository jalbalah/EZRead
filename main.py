

import sys

from SynonymSubstituition import SynonymSubstituition
from CheckRareWord import CheckRareWord


if __name__ == '__main__':
    print(SynonymSubstituition(' '.join(sys.argv[1::])))

sentence = "The word you've entered isn't in the thesaurus.  \
            Click on a spelling suggestion below or try again using the search bar above.  \
            Don't be a convict!"
sentence = 'the cell was surrounded by a phospholipid bi-layer'
sentence = """
    The remains of dozens of people found at a construction site in Texas this year are mostly likely those of African-Americans who were forced to work on a plantation there around the turn of the 20th century, officials said this week.
    That finding, announced Monday, opens a window onto a little-remembered period in which blacks in certain Southern states were essentially treated like slaves post-emancipation.
    The remains of about 95 people were discovered early this year on a construction site outside Houston, where the Fort Bend Independent School District is building a new school, according to school district officials and court records.
    This week, archaeologists announced that the bones were most likely those of African-American laborers who worked as part of the so-called convict lease system, in which the state of Texas outsourced prisoners to work and live on plantations. The researchers estimated that the cemetery, which was on the plantation’s grounds, was used from 1878 to 1911.
    About half of the bodies have been exhumed, and more than 20 have been analyzed. Of those analyzed, archaeologists said, all but one were male, ranging in age from about 14 to 70. All were African-American, and some may have been former slaves.
    It is rare to discover an African-American cemetery from this time period, but rarer still to find a grave site of black prisoners from the convict lease era, said Ken Brown, a professor at the University of Houston who specializes in African-American archaeology.
    You have 3 free articles remaining.
    Subscribe to The Times
    “You have a chance to study what the actual bone material has to say about what life was like — we know it was crappy, we know it was tough — but what impact does all of that have on the body?” he said.
    Researchers hope to run tests that could tell which diseases the prisoners lived with, what kind of foods they ate and where they grew up.
    “It really does change the history books in Texas,” said Reign Clark, a lead archaeologist on site.
    The 13th Amendment to the Constitution abolished slavery in 1865, except as punishment for a crime. Several Southern states, including Texas, used this exception to outsource prisoners for labor, Mr. Brown said.
    EDITORS’ PICKS
    Silicon Valley’s Giants Take Their Talent Hunt to Cambridge
    The Big Business of Becoming Bhad Bhabie
    Where a Taboo Is Leading to the Deaths of Young Girls
    Texas first “leased” out prisoners for caretaking on plantations and later took over the land as state-run prison farms, Mr. Brown said.
    It was “more or less slavery by a new name,” said Reginald Moore, a historian and prison reform advocate who has studied convict leasing in the Houston area.
    He noted that vagrancy laws at the time made it so that blacks were often convicted of minor offenses, such as loitering, and sentenced to years of hard labor in the fields. White prisoners, he said, were often assigned easier work indoors.
    From 1870 to 1912, 60 percent of prisoners in Texas were black, according to the Texas State Historical Association. During this time, prisoners helped build the Capitol building in Austin and constructed part of the Texas State Railroad.
    Today, the Fort Bend Independent School District is building a technical high school on the site of a former sugar plantation that later served as a state-run prison farm.
    After construction workers spotted human bones in February, archaeologists eventually discovered the cemetery on the site, according to court records. In June, a judge granted permission to exhume the remains.
    So far, the results show that the men who were buried there lived difficult lives, researchers said. Their bones show stress from poor health during childhood, such as fever and malnutrition, and stress from repetitive work later in life.
    “They were really doing a lot of heavy labor from the time that they were young,” said Catrina Banks Whitley, a bioarchaeologist who is analyzing the bones.
    Because of that, she said, it is possible that some were former slaves.
    The discovery was particularly gratifying for Mr. Moore, who lives nearby and had long suspected such graves might be hidden there. He has been fighting for recognition for African-American convict laborers, whose role in Texas history, he said, has been mostly forgotten.
    He said he hoped the new findings would encourage Texas to remember them and include their stories in history books and memorials.
    “When I went out there and seen those bodies, I felt so elated that they would finally get their justice,” Mr. Moore said. “It was overwhelming for me. I almost fainted.”
"""