{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [],
   "source": [
    "from collections import Counter \n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###### open log file in read option"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "f = open('access_log2', 'r')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "this lines will take all line in log file and store it in as a element in a list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [],
   "source": [
    "lines = f.readlines()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "to split ip addres from log for number of ip address's present"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [],
   "source": [
    "ip_adrs = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [],
   "source": [
    "for line in lines:\n",
    "    ip_adrs.append(line.split()[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "total ip address in log"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(set(ip_adrs))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Counter({'27.60.182.213': 167,\n",
       "         '::1': 16,\n",
       "         '13.233.58.202': 8,\n",
       "         '87.175.186.81': 1,\n",
       "         '183.87.117.45': 103,\n",
       "         '172.31.9.30': 300,\n",
       "         '171.244.52.131': 1,\n",
       "         '223.189.19.181': 9,\n",
       "         '200.89.105.90': 1})"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Counter(ip_adrs)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "for date and time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [],
   "source": [
    "dt_time = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [],
   "source": [
    "for line in lines:\n",
    "    dt_time.append(line.split()[3])\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "this will find the count of server code / status code occured in it"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [],
   "source": [
    "codes = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [],
   "source": [
    "for line in lines:\n",
    "    codes.append(line.split()[8])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "type status code\t404\n",
      "status code 404 --> count  242\n"
     ]
    }
   ],
   "source": [
    "status = input(\"type status code\\t\")\n",
    "print(f\"status code {status} --> count  {codes.count(status)}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Counter({'403': 1,\n",
       "         '200': 303,\n",
       "         '404': 242,\n",
       "         '301': 8,\n",
       "         '302': 9,\n",
       "         '304': 42,\n",
       "         '400': 1})"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "plot_code = Counter(codes)\n",
    "Counter(codes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "606"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(codes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [],
   "source": [
    "plot_codes = dict(plot_code)\n",
    "\n",
    "server_code = plot_codes.keys()\n",
    "occurence = plot_codes.values()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function matplotlib.pyplot.show(close=None, block=None)>"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.bar(server_code, occurence, color = 'blue' )\n",
    "plt.xlabel('server code')\n",
    "plt.ylabel('occurence')\n",
    "plt.show"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "for finding types of request :- post, get and etc requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [],
   "source": [
    "requests = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [],
   "source": [
    "for line in lines:\n",
    "    requests.append(line.split()[5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Counter({'\"GET': 427, '\"OPTIONS': 16, '\"POST': 163})"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Counter(requests)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
