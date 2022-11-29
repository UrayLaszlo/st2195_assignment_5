{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 210,
   "id": "dd147dca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "328927"
      ]
     },
     "execution_count": 210,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def is_divisible_by_k(x, k):\n",
    " '''\n",
    " Checks whether x is divisible by k.\n",
    " '''\n",
    " return x%k == 0\n",
    "'''\n",
    "Store all the integers that are multiples of 2 or 5 or 7 that are lower\n",
    "or equal to 1000 (excluding doubles)\n",
    "'''\n",
    "x = []\n",
    "for i in range(1001):\n",
    " if (is_divisible_by_k(i, 2) or is_divisible_by_k(i, 5)) or is_divisible_by_k(i, 7):\n",
    "     x.append(i)\n",
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
   "id": "dbce5aa7",
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
