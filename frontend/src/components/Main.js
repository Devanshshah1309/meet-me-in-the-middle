import axios from 'axios';
import React, {useState} from 'react';
import Select from 'react-select';
import makeAnimated from 'react-select/animated';
import {Button, Container} from 'react-bootstrap';
import Locations from './Locations';


const mrtList = [
    'Jurong East', 
    'Bukit Batok',
    'Bukit Gombak',
    'Choa Chu Kang',
    'Yew Tee',
    'Kranji',
    'Marsiling',
    'Woodlands',
    'Admiralty',
    'Sembawang',
    'Canberra',
    'Yishun',
    'Khatib',
    'Yio Chu Kang',
    'Ang Mo Kio',
    'Bishan',
    'Braddell',
    'Toa Payoh',
    'Novena',
    'Newton',
    'Orchard',
    'Somerset',
    'Dhoby Ghaut',
    'City Hall',
    'Raffles Place',
    'Marina Bay',
    'Marina South Pier',
    'Pasir Ris',
    'Tampines',
    'Simei',
    'Tanah Merah',
    'Bedok',
    'Kembangan',
    'Eunos',
    'Paya Lebar',
    'Aljunied',
    'Kallang',
    'Lavender',
    'Bugis',
    'Tanjong Pagar',
    'Outram Park',
    'Tiong Bahru',
    'Redhill',
    'Queenstown',
    'Commonwealth',
    'Buona Vista',
    'Dover',
    'Clementi',
    'Chinese Garden',
    'Lakeside',
    'Boon Lay',
    'Pioneer',
    'Joo Koon',
    'Gul Circle',
    'Tuas Crescent',
    'Tuas West Road',
    'Tuas Link',
    'Expo',
    'Changi Airport',
    'HarbourFront',
    'Chinatown',
    'Clarke Quay',
    'Little India',
    'Farrer Park',
    'Boon Keng',
    'Potong Pasir',
    'Woodleigh',
    'Serangoon',
    'Kovan',
    'Hougang',
    'Buangkok',
    'Sengkang',
    'Punggol',
    'Bras Basah',
    'Esplanade',
    'Promenade',
    'Nicoll Highway',
    'Stadium',
    'Mountbatten',
    'Dakota',
    'MacPherson',
    'Tai Seng',
    'Bartley',
    'Lorong Chuan',
    'Marymount',
    'Caldecott',
    'Botanic Gardens',
    'Farrer Road',
    'Holland Village',
    'one-north',
    'Kent Ridge',
    'Haw Par Villa',
    'Pasir Panjang',
    'Labrador Park',
    'Telok Blangah',
    'Bayfront',
    'Bukit Panjang',
    'Cashew',
    'Hillview',
    'Beauty World',
    'King Albert Park',
    'Sixth Avenue',
    'Tan Kah Kee',
    'Stevens',
    'Rochor',
    'Downtown',
    'Telok Ayer',
    'Fort Canning',
    'Bencoolen',
    'Jalan Besar',
    'Bendemeer',
    'Geylang Bahru',
    'Mattar',
    'Ubi',
    'Kaki Bukit',
    'Bedok North',
    'Bedok Reservoir',
    'Tampines West',
    'Tampines East',
    'Upper Changi'
]

const prefMap = {
    "Cinema": 1,
    "Library": 2,
    "No preference": 3,
    "Museum": 4
}

const mrtOptions = mrtList.map(mrt => ({label: mrt, value: mrt}));
const preferenceOptions = [
    {value: 'No preference', label: 'No preference'}, 
    {value: 'Cinema', label: 'Cinema'}, 
    {value: 'Library', label: 'Library'}, 
    {value: 'Museum', label: 'Museum'}
]

const animatedComponents = makeAnimated();

export default function Main() {
    var [input, setInput] = useState([]);
    var [pref, setPref] = useState(null);
    var [output, setOutput] = useState(null);

    const handleCompute = () => {
        if (input.length < 2) {
            alert("Please provide at least 2 starting points!");
        } else if (pref == null) {
            alert("Please provided your preference!");
        } else {
            let query = `http://127.0.0.1:5000/api/${prefMap[pref.value]}?`;
            input.forEach(point => query += `start=${point.label}&`)
            query = query.substring(0, query.length - 1);
            axios.get(query)
            .then(response => {
                setOutput(response.data.data);
            })
        }
    }

    return (
        <Container>
            <Container id="search" style={{width:"400px"}}>
            <div>
            <h3>Choose your starting points:</h3>
            <Select 
                components={animatedComponents} 
                options={mrtOptions} 
                onChange={setInput}
                placeholder="Select starting points..."
                blurInputOnSelect={true}
                isMulti/>
            </div>
            <div id = "preference">
                <h3>Choose your preference:</h3>
            <Select 
                components={animatedComponents} 
                options={preferenceOptions} 
                onChange={setPref}
                placeholder="Select preference..."
                blurInputOnSelect={true}
                />
            </div>
            
            <Button onClick={handleCompute}> Find us a place!</Button>
        </Container>
        {(output != null) ? <Locations locList={output}/> : null}
        </Container>
        
    )
}
