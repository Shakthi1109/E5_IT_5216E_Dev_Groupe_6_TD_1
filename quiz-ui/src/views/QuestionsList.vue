<template>
  <div class="AdminArea">
    <h3>Admin</h3>
    <router-link to="/question-creation">
      <button class="button">New question</button>
    </router-link>
    <button class="button" @click="clearScoreboard">Delete All Scores</button>
    <button class="button" @click="deleteQuestions">Delete All Questions</button>
    <p></p>
    <h3>Questions List :</h3>
    <div v-for="(question, index) in questionsList" :key="index" @click="editQuestion(question)" class="question-item">
      <div v-if="question">
        Question Number : {{ question.position }} <br>
        Question : {{ question.title }} <br>
        Description : {{question.text}} <br> <br>
      </div>
      <div v-else>
        Question undefinded <br><br>
      </div>
    </div>
    <button @click="logoutAdmin" class="button">Disconnect</button>

    <div v-if="showPopup" class="popup">
      {{ popupMessage }}
    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import QuestionEdition from "@/views/QuestionEdition.vue";

export default {
  name: "QuestionList",
  data() {
    return {
      questionsList: [],
      totalNumberOfQuestion: 0,
      currentQuestion: {
        questionTitle: "",
        questionText: "",
        possibleAnswers: []
      },
      selectedQuestion: null,
      showPopup: false,
      popupMessage: ""
    };
  },
  components: {
    QuestionEdition
  },
  async created() {
    this.getQuestions();
  },
  methods: {
    async getQuestions() {
      console.log("getting questions");
      const quizInfoAPIResult = await quizApiService.getQuizInfo();
      this.totalNumberOfQuestion = quizInfoAPIResult.data.size;
      for (let i = 0; i < this.totalNumberOfQuestion; i++) {
        this.loadQuestionByPosition(i + 1);
      }
      console.log("question list:");
      console.log(this.questionsList);
    },

    async loadQuestionByPosition(currentPosition) {
      var questionInfoAPIResult = await quizApiService.getQuestion(currentPosition);
      this.questionsList[currentPosition - 1] = questionInfoAPIResult.data;
    },

    async editQuestion(data) {
      this.selectedQuestion = data;
      console.log(this.selectedQuestion);
      this.$router.push({ name: "QuestionEdition", params: { myEditedQuestion: JSON.stringify(this.selectedQuestion) } });
    },

    async clearScoreboard() {
      const token = window.localStorage.getItem("token");
      const participationDeleteAPIResult = await quizApiService.deleteParticipation(token);

      this.showPopup = true;
      this.popupMessage = "All participations have been deleted";

      setTimeout(() => {
        this.showPopup = false;
      }, 1000);
    },

    async deleteQuestions() {
      const token = window.localStorage.getItem("token");
      const allQuestionsDeleteAPIResult = await quizApiService.deleteAllQuestions(token);

      this.showPopup = true;
      this.popupMessage = "All questions have been deleted";

      setTimeout(() => {
        this.showPopup = false;
      }, 1000);
    },

    logoutAdmin() {
      this.$router.push("/admin");
    }
  }
};
</script>

<style>
.AdminArea {
  color: white;
  flex-direction: column;
  padding: 2rem;
  margin-top: 5rem;
  color: #FFFFFF;
}

.question-item {
  cursor: pointer;
}

.question-item:hover {
  color: #41d215; /* Change to the desired hover color */
}

.popup {
  position: relative;
  text-align: center;
  color: rgb(255, 0, 0);
  padding: 5rem;
  font-size: 1.2rem;
  border-radius: 5px;
  z-index: 999;
}

.button {
  padding: 12px;
  margin-right: 10px;
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
