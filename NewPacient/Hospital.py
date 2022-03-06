class Hospital:
    listNameOfPacient = []

    def accept(self, name):
        if len(name) > 2:
            self.listNameOfPacient.append(name)

    def recover(self):
        if len(self.listNameOfPacient) == 0:
            return "No more Patients!!!"
        else:
            patient = self.listNameOfPacient.pop(0)
            return f"Recovered Patient: {patient}"
