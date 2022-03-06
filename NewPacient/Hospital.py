class Hospital:
    listNameOfPacient = []

    def accept(self, name):
        if len(name) > 2:
            self.listNameOfPacient.append(name)

    def recover(self):
        if len(self.listNameOfPacient) == 0:
            return "No more Patients!!!"
        else:
            return f"Recovered Patient: {self.listNameOfPacient.pop(0)}"
