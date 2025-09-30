{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ae9f4bdf-e89c-4f43-ac4d-1c970b000b41",
   "metadata": {},
   "source": [
    "## Q4) Condicional (→) – “Uso de PII e base legal"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4fbdff29-f543-4101-9e91-ea5ae05d8a57",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Entradas\n",
    "usa_PII = input(\"O modelo usa PII? \").strip().lower().startswith(\"s\")\n",
    "consentimento_ou_base_legal = input(\"Tem base legal/consentimento? \").strip().lower().startswith(\"s\")\n",
    "\n",
    "\n",
    "if usa_PII and not consentimento_ou_base_legal: # Se o modelo usa PII e não tem base legal, será bloqueado/False\n",
    "    print(\"BLOQUEADO: PII sem base legal.\") \n",
    "else: \n",
    "    print(\"OK: política atendida.\") # Se o modelo usa PII e tem base legal, será atendido/True"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
