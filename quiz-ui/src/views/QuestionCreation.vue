<template>
    <div class="createQuestion">
      <h1>Create question</h1>
      <div >
        <p></p>
        <p>Question Number
        <p>
        <input type="text" v-model="position" />
        </p>
        </p>
        
        <p></p>
        <p>Topic
        <p>
          <input type="text" v-model="title" required />
        </p>
        </p>
        
        <p></p>
        <p>Question
        <p>
          <input type="text" v-model="text" required />
        </p>
        </p>

        <p></p>
        <p>Image
        <p>
          <ImageUpload @file-change="imageFileChangedHandler"/>
        </p>
        </p>
        
        
        
        <p>
        <p>Answers</p>
        <div>
          <input type="text" v-model="possibleAnswer[0]" placeholder="Choice A" />
          <input type="radio" value="0" name="reponse" Checked/>
        </div>
        <div>
          <input type="text" v-model="possibleAnswer[1]" placeholder="Choice B" />
          <input type="radio" value="1" name="reponse"/>
        </div>
        <div>
          <input  type="text" v-model="possibleAnswer[2]" placeholder="Choice C" />
          <input type="radio" value="2"  name="reponse"/>
        </div>
        <div>
          <input  type="text" v-model="possibleAnswer[3]" placeholder="Choice D" />
          <input type="radio" value="3" name="reponse"/>
        </div>
      </p>
    
      </div>
      <button @click="backToQuestionList" class="button">Previous</button>
      <button @click="createQuestion" class="button">Create</button>
    </div>
    </template>
    
<script>
import quizApiService from "@/services/QuizApiService";
import ImageUpload from "@/views/ImageUpload.vue";
export default {
  name: "QuestionCreation",
  data() {
    return {
      position:"",
      title:"",
      text:"",
      image:"",
      possibleAnswer : [],
      selectedAnswer : 0,
      totalNumberOfQuestion : 0
    }
  },
  components:{
    ImageUpload
  },
  async created() {
    const quizInfoAPIResult = await quizApiService.getQuizInfo();
    var quizInfo = quizInfoAPIResult.data.size;
    this.totalNumberOfQuestion= quizInfo;
  },
  methods:{
    imageFileChangedHandler(b64String) {
      this.image = b64String;
    },
    async createQuestion(){
      var reponse = document.querySelector('input[name="reponse"]:checked').value;
      console.log(reponse);
      var possibleAnswers = [];
      for (var i = 0; i < 4; i++){
        var isCorrect = true;
        if (i != parseInt(reponse))
            isCorrect = false;
        else
          isCorrect = true;
        var object = {
          "text" : this.possibleAnswer[i],
          "isCorrect" : isCorrect
        }
        possibleAnswers.push(object);
      }

      // La position, insertion ou ajout !
      this.position = parseInt(this.position, 10);
      if (!this.position || isNaN(this.position)) {
        this.position = this.totalNumberOfQuestion + 1;
        console.log("Good !");
      }
      var question = {
        "position": this.position,
        "title": this.title,
        "text": this.text,
        "image": this.image,
        "possibleAnswers": possibleAnswers
      }
      console.log(question);
      const token = window.localStorage.getItem("token");
      const quizInfoAPIResult = await quizApiService.createQuestion(question, token);
      console.log(quizInfoAPIResult);
      this.$router.push('/question-list');
    },
    backToQuestionList(){
      this.$router.push('/question-list');
    }
  }
}; 
</script>
<style>
.createQuestion{
  color: white;
  flex-direction: column;
  padding: 2rem;
  margin-top: 5rem;
  color: #FFFFFF;
  text-align: center;
}

.button {
  padding: 12px;
  background: #41d215;
  font-size: 15px;
  color: white;
  border: 3px solid #ffffff;
  border-radius: 8px;
  margin-top: 1em;
  cursor: pointer;
  flex-direction: column;
  justify-content: flex-start;
}

.button:hover {
  color: #000000;
}
</style>
 