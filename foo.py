{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3ec97858",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (1127610346.py, line 12)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"/var/folders/06/kkh22cm93nsbkc86_qszf_l80000gp/T/ipykernel_1428/1127610346.py\"\u001b[0;36m, line \u001b[0;32m12\u001b[0m\n\u001b[0;31m    if (is_divisible_by_k(x, 2) & is_divisible_by_k(x, 3)) |\u001b[0m\n\u001b[0m                                                            ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "def is_divisible_by_k(x, k):\n",
    " '''\n",
    " Checks whether x is divisible by k.\n",
    " '''\n",
    " assert x%k == 0\n",
    "'''\n",
    "Store all the integers that are multiples of 2 or 5 or 7 that are lower\n",
    "or equal to 1000 (excluding doubles)\n",
    "'''\n",
    "x = ()\n",
    "for i in range(1000):\n",
    " if (is_divisible_by_k(x, 2) & is_divisible_by_k(x, 3)) |\n",
    "is_divisible_by_k(x, 7):\n",
    " x.append(i)\n",
    "\n",
    "'''\n",
    "Sum all the integers that are multiples of 2 or 5 or 7 that are lower\n",
    "or equal to 1000 (excluding doubles)\n",
    "'''\n",
    "sum(x)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e06925df",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
