---
title: PySpecTools
revealOptions:
    transition: 'fade'
    transition-speed: 'fast'
    width: '100%'
    height: '100%'
    center: false
    margin: 0
    minScale: 1
    maxScale: 1
    symbolperslideprogress:
        position: 'left'
        align: 'vertical'
        symbolColor: ""
        symbolActiveColor: ""
    menu:
        side: "left"
        width: "normal"
    tableofcontents:
        title: ""
        position: 2
        titleTag: "h1"
        titleTagSelector: "h1, h2, h3"
        ignoreFirstSlide: true

---

<!-- .slide: data-background-video="figures/RingSpace.mp4" data-background-video-loop="true" -->

# `PySpecTools`

## Pythonic and Deep Learning Workflows for Spectroscopy

### _Kelvin Lee_, Alexander MacLeod, Michael C. McCarthy

<div class="footer">
    <img src="figures/CfA_Logo_Horizontal_Reverse.svg">
</div>

---

<!-- .slide: data-background="https://cdn.eso.org/images/screen/alma-jfs-2010-10.jpg" -->

# Radio Astronomy

- Observations at radio wavelengths ($\lambda$~submm‒metre)
- Transparent to absorption by interstellar dust
- Powerful inteferometry; high bandwidth, spatial, and spectral resolution

<footer>
    <p>Credit: ESO/ALMA/NRAO</p>
</footer>

----

<div class="column">
    <p>Black Hole Imaging</p>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Black_hole_-_Messier_87_crop_max_res.jpg/1024px-Black_hole_-_Messier_87_crop_max_res.jpg">
    <figcaption>Credit: EHT/NSF/ALMA/SMA/IRAM/JCMT/LMT/SMT</figcaption>
</div>

<div class="column">
    <p>Circumstellar Shells</p>
    <img src="https://www.aanda.org/articles/aa/full_html/2018/02/aa31619-17/aa31619-17-fig3.jpg">
    <figcaption>DOI: <a href="https://www.aanda.org/articles/aa/abs/2018/02/aa31619-17/aa31619-17.html">10.1051/0004-6361/201731619 <a> </figcaption>
</div>

<footer>

<p style="font-size: 1rem">
Astrophysical objects imaged with exquisite detail!
</p>

</footer>

----

# Molecular Astrophysics

<div id="left">

- Molecules reveal physical and chemical properties of space.
    - Gas temperature, density, and velocity
- Microscopic understanding of macroscopic processes;
    - Stellar evolution, planet formation, atmospheres
- Extremely complicated molecular spectra

</div>

<div id="right">

</div>

----

# Zoom and Enhance

<div id="left">

- Spectroscopic analysis extremely manual and labor intensive
- Hundreds to thousands of spectral features (molecular and interference)
- Difficult to automate, reproduce, and catalog
- Analysis rate incommensurate with data acqusition

</div>

<div id="right">

<img src="figures/patel_irc_64GHz.svg" class="inverted">

</div>

----

# Assigning multicomponent spectra

## Constraints

<div id="left">

Number of components are unknown.

No more sample—you had your shot at the experiment. 

This means:

- No double resonance linkages
- No composition tests
- No discharge or magnet tests

</div>

<div id="right">

<div class="fragment">

<p> How do we make the most out of this situation? </p>

</div>

<div class="fragment">

<p> ...How do we do it quickly? </p>

</div>

</div>

----

# Separation of variables

There are two distinct steps to assigning spectra:

1. Finding the most likely sequences of lines;

2. How differentiable are the sequences from random frequencies?

<br>

<strong> Probabilistic models to the rescue! </strong>

---

# The Data

1.6 million asymmetric top spectra with quartic distortion

Parameters uniformly sampled from 1000‒40000 MHz ($A,B,C$).

Additional 600,000 spectra with only $a,b,c$-type fundamental transitions.


---

# An Approximate Hamiltonian

<div id="left">

Use a recurrent encoder-decoder model to evaluate sequences without evaluating a Hamiltonian

For a set of $n$ frequencies $\nu$, we want to evaluate:

$$ \nu_n \vert \nu_{n - 1}, \nu_{n - 2}, \ldots, \nu_{0} $$

In other words, what is the next frequency if I have $n$ frequencies?

Real molecular sequences should follow some parametrized model, while noise should not!

</div>

<div id="right">

<img src="figures/recurrent-encoder-decoder.png" style="width: 450px">

</div>

----

# Encoder

<div id="left">

The encoder model learns to compress information about a sequence of frequencies—like parameters of a Hamiltonian ($z$)

$$ z \vert \nu_n, \nu_{n-1},\ldots $$

we refer to $z$ as an "encoding"/"embedding" vector.

LSTM model learns to produce useful embeddings by training a classifier to predict $a,b,c$-type spectra as softmax likelihoods:

$$ \mathrm{softmax(x)} = \frac{\exp(x)}{\sum \exp(x)} $$

</div>

<div id="right">

<img class="inverted" src="figures/recurrent-encoder-decoder.png" style="width: 450px">

</div>

----

# A good embedding

<div id="left">

Representation of spectra should be readily differentiable

UMAP visualization compares 2D projections of raw spectra and encodings

Raw spectra are 60,000 sets of fundamental transitions

Embeddings are representations of 100,000 asymmetric top spectra

Classification accuracy >90% for all three types for 1.6 M spectra

</div>

<div id="left">

<img src="figures/embedding-viz.png" style="width: 850px">

</div>

----

# A good decoder

<div id="left">

Decoder model uses embedding as initial state, and predicts a frequency given a frequency.

Analogy is predicting transitions, given a Hamiltonian model and parameters.

Mean squared error for 1.6 M spectra is ~0.03%; few MHz at ~13 GHz.

Reproduction accuracy is not essential—that's what the discriminator is for!

</div>

<div id="right">

<img src="figures/recurrent-encoder-decoder.png" style="width: 450px">

</div>

----

# Discriminator

<div id="left">

Discriminator estimates likelihood of sequence to be noise or "real" molecule

Haven't measured actual accuracy yet, but training/validation error is promising

</div>

<div id="right">

<img src="figures/recurrent-encoder-decoder.png" style="width: 450px">

</div>

---

# Finding Sequences

Working with Kyle on a model similar to computer vision/object detection to find sequences.

Also investigating deep reinforcement learning to train neural network to find most likely sequences.

---

<div class="grid sidebar">
    <h1> Thank you! </h1>
</div>

<div class="l-multiple">
    <div class="img-frame">
        <img src="figures/twitter.png" class="end-icons">
        <span>@cmmmsubmm</span>
    </div>
    <div class="img-frame">
        <img src="figures/www.png" class="end-icons">
        <span>laserkelvin.github.io</span>
    </div>
    <div class="img-frame">
      <img src="figures/Octocat.png" class="end-icons">
      <span>@laserkelvin</span>
    </div>
</div>

<footer>

Copyright © 2020 Kelvin Lee

</footer>