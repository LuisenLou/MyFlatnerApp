import { createStore, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import rootReducer from './redux/reducers';


const initialState = {
};

const middleware = [thunk];

const store = createStore(
    rootReducer,
    initialState,
    applyMiddleware(...middleware)
    //composeWithDevTools(applyMiddleware(...middleware))
)
   
export default store;