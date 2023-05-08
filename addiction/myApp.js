var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope) {
  $scope.first=function(){
    $scope.uname= "Hello " +$scope.myname+ " ";
    $scope.content=" we appreciate you for visiting this website.Your data will not be saved you can trust our site. If you Have any addiction we try our best to quit the addiction. Addicare will help you.";
    $scope.visit="block";
    $scope.drugs=document.getElementById("drugs").value;
    if (drugs ="drinking"){
      $scope.go="drinking.html";
    }
    else if(drugs==="smoking") {
      $scope.go="smoking.html";
    }
    
    
    
  }

  $scope.second=function(){
    
  }

});