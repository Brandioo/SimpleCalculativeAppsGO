from Hospital import Hospital

def test_hospital():
    hos = Hospital()

    #accept patients
    hos.accept("Sokoli")
    hos.accept("Goni")
    hos.accept("Bora")
    hos.accept("Genti")
    hos.accept("Albani")

    assert hos.recover() == "Recovered Patient: Sokoli"
    assert hos.recover() == "Recovered Patient: Goni"
    assert hos.recover() == "Recovered Patient: Bora"
    assert hos.recover() == "Recovered Patient: Genti"
    assert hos.recover() == "Recovered Patient: Albani"
    assert hos.recover() == "No more Patients!!!"