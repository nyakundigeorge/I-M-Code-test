/**
 * Author: George Nyakundi
 * Date: 29/01/2019
 * Role: Perform queries to https://swapi.co/api/
 * 
 * and displays a list of the Star Wars characters’ attributes (at least 3) in a table.
 *  When a user clicks on an element, they should be able to view all the details for the selected character.
 *  The user should be allowed to open a character’s details in a new tab.
 *   The detail view should have a favorites feature where they can pick up to 5 favorites from of the list.
 * They should also be able to remove a character from their list of favorites.
 * If a character is marked as a favorite, this should be indicated in the list view with a heart icon.

 */

async function fetchData() {
   
    const records = await fetch('https://swapi.co/api/people/');
    const people_records = await records.json();
    
    return people_records;
}

 async function loadPage() {
    let all_people = await fetchData();
    let all_people_result = all_people.results
    var tbody = document.getElementById('tbody');

    for(var i = 0;i< all_people_result.length;i++){
        let tr = "<tr><td>" + i + "</td> <td>" + all_people_result[i]['name'] + "</td> <td>" + all_people_result[i]['birth_year'] + "</td><td>" + all_people_result[i]['gender'] + "</td><td>" + all_people_result[i]['skin_color'] + "</td><td>" + 'View Details'+ "</td><td>" + 'Favorite'+ "</td></tr>";
        tbody.innerHTML += tr;
    }

    
    
    console.log(all_people)

}

loadPage()
/**
 * 
 */
function loadDetails(){

}
/**
 * The Details view should have a favorites feature where a user can pick up to 5 favorites.
 * 
 */
function markFavorite() {

}


/**
 * we'll be calling this function to get the favorites from the local storage and append a heart icon next to it.
 */
function getFavorites() {

}

/**
 * This function will be for removing a character from the favorites stored in localstorage
 */
function removeFavorites() {

}

function getDetails() {

}