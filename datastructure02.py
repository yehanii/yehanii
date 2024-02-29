ProgramLanguage=["c언어","C++","JAVA","Java Script"]
ProgramBook=["c언어 길라잡이","Do it! JAVA"]
ProgramLanguage  +=ProgramBook
print(ProgramLanguage)
del ProgramLanguage[2]
print(ProgramLanguage)

del ProgramLanguage[ProgramLanguage.index("C++")]
print(ProgramLanguage)