
console.log("connected"); 
var app = angular.module('mainApp', []).config(function($interpolateProvider){
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
});
app.controller("mainController", function ($scope) {
	$scope.numSlots = 48; 	
	$scope.AMSched = 0; 
	$scope.PMSched = 0; 
    $scope.weekCount = 0; 
	$scope.datesToDisplay = 100; 
	$scope.dateArray = []; 
    $scope.datesThisWeek = []; 
	$scope.slotsForRepeat = []; 
	$scope.date = new Date(); 
	$scope.username = ""; 

    for (var i = 0; i < $scope.numSlots; i++) {
      	$scope.slotsForRepeat.push(i); 
    }
    $scope.days = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]; 


	var start = new Date()
    for (var i = 0; i < $scope.datesToDisplay; i++) {
    	$scope.dateArray.push(start);
    	var newDate = start.setDate(start.getDate() + 1);
       	start = new Date(newDate);
    }

    $scope.changeWeek = function (num) {
        $scope.weekCount = $scope.weekCount + num; 
        //getCurrentWeek(); 
    }

    function getCurrentWeek () {
        for (var i = $scope.weekCount; i < $scope.weekCount + 7; i++) {
            $scope.datesThisWeek.push($scope.dateArray[i]); 
        }
    }


    $scope.toggleAMBits = function (slot) {
    	mask = 1 << slot; 
    	$scope.AMSched = $scope.AMSched ^ mask; 
    }

    $scope.togglePMBits = function (slot) {
    	temp = slot - 24; 
    	mask = 1 << temp; 
    	$scope.PMSched = $scope.PMSched ^ mask; 
    }

    $scope.setDate = function (date) {
    	$scope.date = date; 
    }

}
)
