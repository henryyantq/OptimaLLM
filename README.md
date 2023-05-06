# OptimaLLM

**Attention! Please replace YOUR_OPENAI_API_KEY with your personal valid OpenAI API key.**

Requirements: `pip install httpx` or `pip3 install httpx`

The official implementation of the paper *Refining the Responses of LLMs by Themselves*. In this paper, we propose a simple yet efficient approach based on prompt engineering that leverages the large language model itself to optimize its answers without relying on auxiliary models. We introduce an iterative self-evaluating optimization mechanism, with the potential for improved output quality as iterations progress, removing the need for manual intervention. The experiment's findings indicate that utilizing our response refinement framework on the GPT-3.5 model yields results that are on par with, or even surpass, those generated by the cutting-edge GPT-4 model. Detailed implementation strategies and illustrative examples are provided to demonstrate the superiority of our proposed solution.

<p align="center">
  <br>
  <img src="https://user-images.githubusercontent.com/20149275/236629683-e4fd0122-6f95-414f-9e50-e8071aa01df2.png" alt="Image 1" width="90%" />
  <br>
  <br>
  <img src="https://user-images.githubusercontent.com/20149275/236629603-d96d4496-6130-4b0e-83c0-ac5dc3c973ad.png" alt="Image 2" width="90%" />
  <br>
</p>

**References of our work**

[1] Ashish Vaswani, Noam M. Shazeer, Niki Parmar, Jakob Uszkoreit,
Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. At-
tention is all you need. ArXiv, abs/1706.03762, 2017.

[2] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova.
Bert: Pre-training of deep bidirectional transformers for language un-
derstanding. ArXiv, abs/1810.04805, 2019.

[3] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah,
Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam,
Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss,
Gretchen Krueger, T. J. Henighan, Rewon Child, Aditya Ramesh,
Daniel M. Ziegler, Jeff Wu, Clemens Winter, Christopher Hesse,
Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess,
Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya
Sutskever, and Dario Amodei. Language models are few-shot learners.
ArXiv, abs/2005.14165, 2020.

[4] Zhilin Yang, Zihang Dai, Yiming Yang, Jaime G. Carbonell, Ruslan
Salakhutdinov, and Quoc V. Le. Xlnet: Generalized autoregressive pre-
training for language understanding. In Neural Information Processing
Systems, 2019.

[5] Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaud-
hary, Guillaume Wenzek, Francisco Guzmán, Edouard Grave, Myle
Ott, Luke Zettlemoyer, and Veselin Stoyanov. Unsupervised cross-
lingual representation learning at scale. In Annual Meeting of the Asso-
ciation for Computational Linguistics, 2019.

[6] OpenAI. Gpt-4 technical report. arXiv preprint arXiv:2303.08774,
2023.

[7] Alec Radford and Karthik Narasimhan. Improving language under-
standing by generative pre-training. 2018.

[8] Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, and
Shmargaret Shmitchell. On the dangers of stochastic parrots: Can lan-
guage models be too big? Proceedings of the 2021 ACM Conference on
Fairness, Accountability, and Transparency, 2021.

[9] Yizhe Zhang, Siqi Sun, Michel Galley, Yen-Chun Chen, Chris Brock-
ett, Xiang Gao, Jianfeng Gao, Jingjing Liu, and William B. Dolan. Di-
alogpt : Large-scale generative pre-training for conversational response
generation. In Annual Meeting of the Association for Computational
Linguistics, 2019.

[10] Alex Wang, Yada Pruksachatkun, Nikita Nangia, Amanpreet Singh, Ju-
lian Michael, Felix Hill, Omer Levy, and Samuel R. Bowman. Super-
glue: A stickier benchmark for general-purpose language understanding
systems. ArXiv, abs/1905.00537, 2019.

[11] Paul Francis Christiano, Jan Leike, Tom B. Brown, Miljan Martic,
Shane Legg, and Dario Amodei. Deep reinforcement learning from
human preferences. ArXiv, abs/1706.03741, 2017.

[12] Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wain-
wright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina
Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke E.
Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Francis
Christiano, Jan Leike, and Ryan J. Lowe. Training language models
to follow instructions with human feedback. ArXiv, abs/2203.02155,
2022.

[13] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed Huai
hsin Chi, F. Xia, Quoc Le, and Denny Zhou. Chain of thought prompt-
ing elicits reasoning in large language models. ArXiv, abs/2201.11903,
2022.
